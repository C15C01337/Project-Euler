# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


# define a function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# define a list of the number of days in each month, in order
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

# initialize a counter for the number of Sundays that fall on the first of the month
sunday_count = 0

# initialize a variable to keep track of the day of the week
# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
day_of_week = 1  # 1 Jan 1901 was a Tuesday

# loop over the years from 1901 to 2000
for year in range(1901, 2001):
    # loop over the months from January to December
    for month in range(12):
        # check if the first day of the month is a Sunday
        if day_of_week == 6:
            sunday_count += 1
        # get the number of days in the current month
        num_days = month_days[month]
        # add an extra day if it's February and a leap year
        if month == 1 and is_leap_year(year):
            num_days += 1
        # update the day of the week for the first day of the next month
        day_of_week = (day_of_week + num_days) % 7

print(sunday_count)  # output the result
 