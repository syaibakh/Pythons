from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PL5NE5Aw6LXceuuw9WMc6PZUHC0UteUX2m')

for video in playlist.video:
	print(video.title)
	video.streams.first().download()