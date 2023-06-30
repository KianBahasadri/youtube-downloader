from pytube import YouTube, Playlist

type = input("video or playlist (v/p): ")
URL = input("Enter URL: ")

if (type == "p" or type == "playlist"):

    playlist = Playlist(URL)

    i = 1

    for video in playlist.videos:
        video.streams.get_highest_resolution().download("/Users/justinli/Documents/GitHub/youtube-downloader/downloaded")

        print("Video Downloaded (" + i + "): " + video.title)

    print("All videos in playlist successfully downloaded")

elif (type == "v" or type == "video"):

    # yt = YouTube(URL).streams.first() # selects first result
    yt = YouTube(URL)

    # stream = yt.streams.first()

    video_title = yt.title

    request = input('Download (y/n): "' + video_title + '?"\n')

    if (request == "y"):
        yt.streams.first().download("/Users/justinli/Documents/GitHub/youtube-downloader/downloaded")

        print("Video successfully downloaded")