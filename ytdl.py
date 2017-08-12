import terminal, scraper, os

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

    downloaded_files = get_downloaded_files(path)
    new_videos = find_new_videos(videos_in_playlist, downloaded_files)

def find_new_videos(videos_in_playlist, downloaded_files):
    new_videos = []

    return new_videos

def get_downloaded_files(path):
    files = []

    for file in os.listdir(path):
        if file.endswith(".mp3"):
            files.append(os.path.join(path, file))

    return files

main()
