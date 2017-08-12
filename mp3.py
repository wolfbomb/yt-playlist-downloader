from mutagen.easyid3 import EasyID3

class MP3:
    def __init__(self, path):
        self.tags = EasyID3(path)

    def read_artist(self):
        return read_tag("artist")

    def read_title(self):
        return read_tag("title")

    def read_url(self):
        return read_tag("website")

    def read_tag(self, tag):
        return self.tags[tag]

    def write_tag(self, tag, value):
        self.tags[tag] = value
        self.save()

    def save(self):
        self.tags.save()
