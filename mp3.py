from mutagen.easyid3 import EasyID3
from mutagen.easyid3 import EasyID3KeyError

class MP3:
    def __init__(self, path):
        self.tags = EasyID3(path)

    def read_artist(self):
        return self.read_tag("artist")

    def read_title(self):
        return self.read_tag("title")

    def read_url(self):
        return self.read_tag("website")

    def read_tag(self, tag):
        try:
            return self.tags[tag][0]
        except EasyID3KeyError:
            return ""


    def write_tags(self, tags):
        for tag in tags:
            self.tags[tag] = tags[tag]

        self.save()

    def save(self):
        self.tags.save()

    def has_all_tags():
        if not read_url():

        if not read_artist() or not read_title():

    def set_tags():
        
