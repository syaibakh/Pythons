from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW')

for video in playlist.video:
	print(video.title)
	video.streams.first().download()