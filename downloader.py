import scraper, subprocess
from directory import Directory

class Downloader:
    def __init__(self, path):
        self.directory = Directory(path)

    def find_new_videos(self, url):
        videos_in_playlist = scraper.find_videos_in_playlist(url)

        downloaded_files = self.directory.get_downloaded_files()
        new_videos = self.directory.find_new_videos(videos_in_playlist, downloaded_files)

        return new_videos

    def download_videos(self, videos):
        for video in videos:
            self.download_video(video)

    def download_video(self, video):
        subprocess.call(["youtube-dl", "-x", "--audio-format", "mp3", "-o",
            self.directory.path + ("" if self.directory.path.endswith("/") else "/")
                + "%(title)s.%(ext)s\" \"", video.url]);
