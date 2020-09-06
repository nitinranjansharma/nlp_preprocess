class CaseUnify():
    def __init__(self, text, case='lower'):
        self.text = text
        self.case = case

    def get_data(self):
        if self.case == 'upper':
            return (self.text.upper())
        else:
            return(self.text.lower())


def case_unify(text, case):
    case_char = CaseUnify(text, case)
    return case_char.get_data()
