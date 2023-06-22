from pytube import YouTube

url = "https://www.youtube.com/watch?v=3QhAm5aFEt8"
vid = YouTube(url)

# these three lines below all give me errors idk why
print(vid.title) # output vid name

# vid = vid.streams.get_highest_resolution()
# vid.download()