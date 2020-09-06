import re


class SpecialChar():
    def __init__(self, text):
        self.text = text
        self.mod = ""

    def get_data(self):
        final_text = ""
        for str1 in self.text.split(" "):
            str1 = re.sub('[\W\_]', '', str1)
            self.mod = self.mod+' '+str1
        return (' '.join(self.mod.split()))


def strip_space(text):
    spl_char = SpecialChar(text)
    return spl_char.get_data()
