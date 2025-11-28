import yt_dlp

def download_mp3(youtube_url, output_folder="."):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_folder}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Example
if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_mp3(url, output_folder="downloads")
    print("Download completed!")
