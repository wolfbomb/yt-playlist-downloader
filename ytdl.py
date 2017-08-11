import terminal

def main():
    if terminal.get_argument_count() < 3:
        terminal.print_help()
        exit()
    else:
        firstArg = terminal.get_argument(1)
        secondArg = terminal.get_argument(2)

main()
