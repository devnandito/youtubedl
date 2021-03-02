import youtube_dl

if __name__ == "__main__":
    input_url = input("Enter url:")
    video_info = youtube_dl.YoutubeDL().extract_info(url=input_url, download=False)
    video_title = video_info['title']
    options = {
        'format': 'bestaudio/best',
        'outtmpl': f"/mnt/d/musicYdl/{video_title}.mp3",
        'postprocessor': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([input_url])