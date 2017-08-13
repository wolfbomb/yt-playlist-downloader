import os
from mp3 import MP3

class Directory:
    def __init__(self, path):
        self.path = path
        self.mkdir()

    def mkdir(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def find_new_videos(self, videos_in_playlist, files):
        if len(files) == 0:
            return videos_in_playlist

        new_videos = list(videos_in_playlist)

        for video in videos_in_playlist:
            for file in files:
                if video.url == MP3(file).read_url():
                    new_videos.remove(video)

        return new_videos

    def get_downloaded_files(self):
        files = []

        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                files.append(os.path.join(self.path, file))

        return files

    def check_file_tags(self):
        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                mp3 = MP3(self.path + ("" if self.path.endswith("/") else "/") + file)
                if not mp3.has_all_tags():
                    mp3.set_tags()
                else:
                    print(file + " has all tags: artist=" + mp3.read_artist() + " title=" + mp3.read_title())
