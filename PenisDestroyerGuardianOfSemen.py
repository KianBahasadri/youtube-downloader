from pytube import YouTube
from pytube import Playlist
import os

destination = "/Users/aradm/Downloads" #only works for me
while True:
    url = input()
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
          
    else:
       video = YouTube(url)
       video = video.streams.filter(only_audio=True).first()
       downloadFile = video.download(output_path=destination)
       base, ext = os.path.splitext(downloadFile)
       mp3Name = base + '.mp3'
       os.rename(downloadFile, mp3Name)
       print(video.title + " has been successfully downloaded.")
