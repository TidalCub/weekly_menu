import datetime


def week_number():
    return datetime.datetime.now().isocalendar()[1]