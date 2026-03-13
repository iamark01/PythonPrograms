from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import BackgroundTasks
from typing import Any, cast

import yt_dlp, yt_dlp.utils
import os, uuid, json

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
static_dir = BASE_DIR /  "static"
template_dir = BASE_DIR /  "templates"
DOWNLOAD_DIR = BASE_DIR /  "downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)
HISTORY_FILE = BASE_DIR /  "history.json"

templates = Jinja2Templates(directory=template_dir)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

if not HISTORY_FILE.exists():
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_info")
def get_info(url: str = Form(...)):
    try:
        ydl_opts: dict[str, Any] = {"quiet": True, "skip_download": True}

        with yt_dlp.YoutubeDL(cast(Any, ydl_opts)) as ydl:
            info = ydl.extract_info(url, download=False)

        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "thumbnail": info.get("thumbnail"),
        }

    except Exception as e:
        return {"error": str(e)}


@app.post("/convert")
def convert(url: str = Form(...)):
    file_id = str(uuid.uuid4())

    ydl_opts: dict[str, Any] = {
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        # "max_filesize": 50_000_000,  # 50MB
        "outtmpl": str(DOWNLOAD_DIR / f"{file_id}.%(ext)s"),
        "retries": 10,
        "fragment_retries": 10,
        "skip_unavailable_fragments": True,

        "sleep_interval": 2,
        "max_sleep_interval": 5,
        
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
            },

        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
                }
                },

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    try:
        with yt_dlp.YoutubeDL(cast(Any, ydl_opts)) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError:
        return {
            "success": False,
            "error": "Unable to download video (403 or restricted video)."
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

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
        "success": True,
        "download": f"/download/{file_id}",
    }


@app.get("/download/{file_id}")
def download(file_id: str):

    file_path = DOWNLOAD_DIR / f"{file_id}.mp3"
    print(file_path)

    if not file_path.exists():
        return {"error": "File not found"}

    return FileResponse(
        file_path,
        media_type="audio/mpeg",
        filename="audio.mp3"
    )

@app.get("/history", response_class=HTMLResponse)
def history_page(request: Request):
    with open(HISTORY_FILE, "w") as f:
        history = json.load(f)
    return templates.TemplateResponse("history.html", {"request": request, "history": history})
