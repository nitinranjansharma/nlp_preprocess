from io import StringIO
from html.parser import HTMLParser


class HTMLStrip(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    htmlStripperObj = HTMLStrip()
    htmlStripperObj.feed(html)
    return htmlStripperObj.get_data()
