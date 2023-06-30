from pytube import YouTube, Playlist

URL = input("Enter YouTube URL: ")

if "list" in URL:
    pass

    playlist = Playlist(URL)

    i = 1

    for video in playlist.videos:
        video.streams.get_highest_resolution().download()

        print("Video Downloaded (" + i + "): " + video.title)

    print("All videos in playlist successfully downloaded")

else:

    # yt = YouTube(URL).streams.first() # selects first result
    yt = YouTube(URL)

    # stream = yt.streams.first()

    video_title = yt.title

    request = input('Download (y/n): "' + video_title + '?"\n')

    if (request == "y"):
        yt.streams.first().download()

        print("Video successfully downloaded")