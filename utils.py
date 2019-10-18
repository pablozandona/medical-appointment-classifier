from dateutil.parser import parse

def get_day_distance(day1, day2):
    return (parse(day1) - parse(day2)).days
