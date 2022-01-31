from pytube import YouTube

DOWNLOAD_FOLDER = "C:\\Users\\usuario\\Downloads"

video_url = "https://www.youtube.com/watch?v=Y3VEa8B5cZ8"

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)