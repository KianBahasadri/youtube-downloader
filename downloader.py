from pytube import YouTube

url = "https://www.youtube.com/watch?v=3QhAm5aFEt8"
vid = YouTube(url)

print(vid.title)
