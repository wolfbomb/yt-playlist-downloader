import terminal, scraper
from directory import Directory

def main():
    if terminal.get_argument_count() < 3:
        terminal.print_help()
        exit()
    else:
        firstArg = terminal.get_argument(1)
        secondArg = terminal.get_argument(2)

        if firstArg == "help":
            terminal.print_help()
        else:
            download_playlist(firstArg, secondArg)

def download_playlist(url, path):
    videos_in_playlist = scraper.find_videos_in_playlist(url)

    directory = Directory(path)
    downloaded_files = directory.get_downloaded_files()
    new_videos = directory.find_new_videos(videos_in_playlist, downloaded_files)

main()
