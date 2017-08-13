import fails, os, re
from mutagen.easyid3 import EasyID3
from mutagen.easyid3 import EasyID3KeyError

class MP3:
    def __init__(self, path):
        self.path = path
        self.tags = EasyID3(self.path)

    def read_artist(self):
        return self.read_tag("artist")

    def read_title(self):
        return self.read_tag("title")

    def read_url(self):
        return self.read_tag("website")

    def read_tag(self, tag):
        try:
            if tag in self.tags:
                return self.tags[tag][0].encode("utf-8")
            else:
                return ""
        except EasyID3KeyError:
            return ""


    def write_tags(self, tags):
        for tag in tags:
            self.tags[tag] = tags[tag].decode("utf-8")

        self.save()

    def save(self):
        self.tags.save()

    def has_all_tags(self):
        if not self.read_url():
            fails.add_fail(self.path)
            return False

        if not self.read_artist() or not self.read_title():
            return False

        return True

    def set_tags(self):
        filename_with_ext = os.path.basename(self.path)
        filename = os.path.splitext(filename_with_ext)[0]
        filename = self.remove_square_brackets(filename)

        if "-" in filename:
            artist = filename[:filename.index("-")].strip()
            title = filename[filename.index("-")+1:].strip()
            self.write_tags({"artist": artist, "title": title})

    def remove_square_brackets(self, str):
        return re.sub(r'\[.*?\]', '', str)
