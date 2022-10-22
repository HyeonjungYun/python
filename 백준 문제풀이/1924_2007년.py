from datetime import datetime, date

def whatweek(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    print(days[day])
a, b = map(int,input().split())
whatweek(date(2007, a, b))