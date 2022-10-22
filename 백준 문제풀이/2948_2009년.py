from datetime import datetime, date

def whatweek(date):
    days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = date.weekday()
    print(days[day])
a, b = map(int,input().split())
whatweek(date(2009, b, a))