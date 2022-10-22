from pytube import YouTube
from sys import argv 

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution() #this insures that the video will be downloaded in the highest resolution possible 

yd.download('C:/Users/alcha/Videos/YoutubeDownloads')