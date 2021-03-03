import youtube_dl, os
from pydub import AudioSegment


def menu():
    print('Select options')
    print('\t1 Clean screen')
    print('\t2 Exit')
    print('\t3 Download video to mp3')
    print('\t4 Convert wav to mp3')
    print('\t5 Convert mp3 to wav')

if __name__ == "__main__":
    while True:
        menu()
        option = input("Enter option:")
        if option == '1':
            os.system('clear')
        elif option == '2':
            break
        elif option == '3':
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
        elif option == '4':
            src = input("Enter wav:")
            dst = input("Enter mp3 name:")
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
        elif option == '5':
            src = input("Enter mp3:")
            dst = input("Enter wav name:")
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
        else:
            continue