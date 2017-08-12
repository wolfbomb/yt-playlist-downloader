class Video:
    def __init__(self, title, url):
        self.title = title
        self.url = "https://www.youtube.com" + self.remove_url_parameters(url)

    def remove_url_parameters(self, url):
        head, separator, tail = url.partition("&")
        return head
