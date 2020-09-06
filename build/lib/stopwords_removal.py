class StopWords():
    def __init__(self, text, stop_list):
        self.text = text
        self.stop_list = stop_list

    def get_data(self):
        return(' '.join([i for i in self.text.split(" ") if i not in self.stop_list]))


def rem_stopwords(text, stop_list):
    rem_stop = StopWords(text, stop_list)
    return rem_stop.get_data()
