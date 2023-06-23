from pytube import YouTube

vid = input("Enter YouTube URL: ")

# yt = YouTube(vid).streams.first()
yt = YouTube(vid) # the above line gives error for some reason

video_title = yt.title

request = input('Download (y/n): "' + video_title + '?"\n')

if (request == "y"):
    yt.download()