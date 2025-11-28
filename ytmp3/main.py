from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import yt_dlp
import os, uuid, json

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

HISTORY_FILE = "history.json"

if not os.path.exists("downloads"):
    os.makedirs("downloads")

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_info")
def get_info(url: str = Form(...)):
    """Extract video info (title, duration, thumbnail) before converting."""
    ydl_opts = {"quiet": True, "skip_download": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail"),
    }


@app.post("/convert")
def convert(url: str = Form(...)):
    file_id = str(uuid.uuid4())
    mp3_path = f"downloads/{file_id}.mp3"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"downloads/{file_id}.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Save history entry
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    history.append({
        "id": file_id,
        "url": url
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

    return {
        "download": f"/download/{file_id}",
    }


@app.get("/download/{file_id}")
def download(file_id: str):
    file_path = f"downloads/{file_id}.mp3"
    return FileResponse(file_path, media_type="audio/mpeg", filename="video.mp3")


@app.get("/history", response_class=HTMLResponse)
def history_page(request: Request):
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    return templates.TemplateResponse("history.html", {"request": request, "history": history})
