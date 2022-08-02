# App  allowing to download Youtube videos

from pytube import YouTube
from sys import argv

# asks user to paste the link
link = input("Please paste the youtube link: ")

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

# here you can change location
yd.download('./DownloadedVideos/')
