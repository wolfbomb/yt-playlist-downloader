import sys, colorama

colorama.init(autoreset=True)

def get_argument_count():
    return len(sys.argv)

def get_argument(index):
    return sys.argv[index]
