from distutils.core import setup

setup(
	name = "YT-Playlist-Downloader",
	version = "1.0",
	description = "A command-line program for downloading YT-playlists.",
	author = "Nicolas Raube",
	packages = ["modules"],
	scripts = ["ytdl.py"]
)
