from dateutil.parser import parse

datetime = parse('2018-06-29 22:21:41')

def get_day_distance(day1, day2):
    return (parse(day1) - parse(day2)).days
