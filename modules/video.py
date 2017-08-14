class Video:
    def __init__(self, title, url, path):
        self.title = title
        self.url = "https://www.youtube.com" + self.remove_url_parameters(url)
        self.path = path + ("" if path.endswith("/") else "/") + self.title + ".mp3"

    def remove_url_parameters(self, url):
        head, separator, tail = url.partition("&")
        return head
