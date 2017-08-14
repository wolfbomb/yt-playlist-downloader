import terminal, fails
from downloader import Downloader

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
            downloader = Downloader(secondArg)

            new_videos = downloader.find_new_videos(firstArg)
            terminal.print_green(str(len(new_videos)) + " new videos found")

            downloader.download_videos(new_videos)

            for fail in fails.fails:
                terminal.print_red("failed: " + fail.path)

main()
