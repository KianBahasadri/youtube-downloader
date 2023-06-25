from pytube import YouTube
from pytube import Playlist
import os

destination = "/Users/aradm/Downloads" # only works for me

while True:
    url = input("Enter playlist URL: ")

   # idea: use 'playlist.video_urls' to get all the URLs in the playlist, then for loop through it
   # this ensures all the videos in the playlist are downloaded if the user enters the URLs of a video in a playlist that is NOT the first one

    if 'list' in url:
       playlist = Playlist(url)
       print(len(playlist.video_urls))

       for video in playlist.videos:
          video = video.streams.filter(only_audio=True).first()
          print(video.title)

          downloadFile = video.download(output_path=destination)
          base, ext = os.path.splitext(downloadFile)
          mp3Name = base + '.mp3'

          os.rename(downloadFile, mp3Name)

          print(video.title + " has been successfully downloaded.")
          
    else: # if URL is not a playlist
       video = YouTube(url)
       video = video.streams.filter(only_audio=True).first()
       downloadFile = video.download(output_path=destination)
       base, ext = os.path.splitext(downloadFile)
       mp3Name = base + '.mp3'

       os.rename(downloadFile, mp3Name)
       print(video.title + " has been successfully downloaded.")
