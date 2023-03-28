class NegativeTitlesError(Exception):
    def __init__(self):
        self.message = "titles cannot be negative"


class InvalidYearCupError(Exception):
    def __init__(self):
        self.message = "there was no world cup this year"


class ImpossibleTitlesError(Exception):
    def __init__(self):
        self.message = "impossible to have more titles than disputed cups"
