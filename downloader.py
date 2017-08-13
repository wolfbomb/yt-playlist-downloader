import scraper
from directory import Directory

def find_new_videos(url, path):
    videos_in_playlist = scraper.find_videos_in_playlist(url)

    directory = Directory(path)
    downloaded_files = directory.get_downloaded_files()
    new_videos = directory.find_new_videos(videos_in_playlist, downloaded_files)

    return new_videos
