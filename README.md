# YouTube Playlist Downloader
yt-playlist-downloader is a command-line tool that downloads every video in a YouTube playlist as an MP3-file and automatically adds id3 tags to them. Those tags allow MP3 players to display information about a song such as the author or title.
It also detects new videos in the playlist and downloads only those.

This project uses [youtube-dl](https://github.com/rg3/youtube-dl) by [Ricardo Garcia](https://github.com/rg3) to download YouTube videos.

## Automatic tag setting
yt-playlist-downloader automatically sets the following MP3 tags (ID3):
#### Artist
Usually the first part of the YT-title
#### Title (of the song)
Usually the second part of the YT-title
#### Website
The YouTube-URL of the video which is used for comparing local MP3-files to the videos in a playlist.

For auto tag-setting to work flawlessly, the YT-title of the video must follow the following pattern:
<br><b>Artist - Title (additional information)</b><br>
If the YT-title contains exactly one dash ('-'), the left part of it will be used as the artist tag and the right part will be used as the title tag. Otherwise, the user will be prompted to enter the artist and song title after the whole download process finished.
Square brackets ('[ ]') and everything inside them will be removed from the title, as well as these characters: ' \ / " . _

## Installation
Clone the repository to your computer by running:
```git clone https://github.com/nicolasraube/yt-playlist-downloader.git```

Install [Python](https://www.python.org/downloads/)

Now install the following Python modules with pip (should come with Python):
```pip install colorama requests mutagen beautifulsoup4```

You are now ready to use yt-playlist-downloader.
