class WhitespaceCorrect():
    def __init__(self, text):
        self.text = text

    def get_data(self):
        return (' '.join(self.text.split()))


def strip_space(text):
    whitespace = WhitespaceCorrect(text)
    return whitespace.get_data()
