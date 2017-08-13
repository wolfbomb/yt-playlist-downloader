fails = []

def add_fail(file):
    fails.append(file)

def add_fails(files):
    for file in files:
        add_fail(file)
