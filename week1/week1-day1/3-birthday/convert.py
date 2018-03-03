import time
import datetime
from datetime import timedelta
# from dateutil.relativedelta import relativedelta

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def PrintResults(ref_dt):
    # get todays date
    today = datetime.date.today()

    # compute date difference between reference date and today
    date_diff = today - ref_dt

    # print results
    print('today: ', today)
    print('ref_date: ', ref_dt)

    dMonths = diff_month(today, ref_dt)

    print('months:  ', dMonths)
    print('days:    ', date_diff.days)
    print('hours:   ', date_diff.days * 24)
    print('minutes: ', date_diff.days * 24 * 60 )


def age_to_time(age):
    # get 1 year in datetime format
    year = timedelta(days=365)

    # current age = input age in years * 1 year
    cur_age = age * year

    # get todays date
    today = datetime.date.today()

    # reference date = today - age in years
    ref_date = today - cur_age
    PrintResults(ref_date)



def birthday_to_time(birthday):
    PrintResults(birthday)

#str_age = input('Enter your age: ')
#age = int(str_age)
#age_to_time(age)

str_birthday = raw_input('When were you born?')

date_parts = str_birthday.split('-')

month = int(date_parts[0])
day   = int(date_parts[1])
year  = int(date_parts[2])

birthday = datetime.date(year, month, day)

birthday_to_time(birthday)



