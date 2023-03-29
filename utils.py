from datetime import datetime

from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(data):
    if data["titles"] < 0:
        raise NegativeTitlesError()

    first_cup = datetime.strptime(data["first_cup"], "%Y-%m-%d")
    if first_cup.year < 1930 or (first_cup.year - 1930) % 4 != 0:
        raise InvalidYearCupError()

    now = datetime.now()
    max_titles = (now.year - first_cup.year) // 4 + 1
    if data["titles"] > max_titles:
        raise ImpossibleTitlesError()
