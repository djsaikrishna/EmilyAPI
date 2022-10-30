from html.parser import HTMLParser


class OHTMLParser(HTMLParser):
    def __init__(self):
        self.found = False
        self.val = None
        return HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs and attrs["id"] == "surl":
            self.found = True

    def handle_data(self, data):
        if not self.found:
            return
        if data.startswith("http://osdb"):
            self.val = data
