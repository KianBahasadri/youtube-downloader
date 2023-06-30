from pytube import YouTube, Playlist

URL = input("Enter YouTube URL: ")

if list in URL:
    pass

    playlist = Playlist(URL)

    for video in playlist.videos:
        video.streams.get_highest_resolution().download()


else:

    # yt = YouTube(vid).streams.first()
    vid = YouTube(URL) # the above line gives error for some reason

    video_title = vid.title

    request = input('Download (y/n): "' + video_title + '?"\n')

    if (request == "y"):
        vid.download("/Users/justinli/Downloads")

    # git push update test