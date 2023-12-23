# Exercise: day 16

# Get the current day, month, year, hour, minute and timestamp from datetime module
import datetime as dt
now = dt.datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

# Format the current date using this format:"%m/%d/%Y,%H:%M:%S")
print(now.strftime("%m/%d/%Y"))
print(now.strftime("%H:%M:%S"))

# Today is 22 December, 2023. Change this time string to time.
date_string = "22 December, 2023"
print("date_string =", date_string)

# calculate the time difference between now and new year.
today = dt.date(year=2023, month=12, day=22)
new_year = dt.date(year=2024, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

# calculate the time difference between 1 January 1970 and now
old = dt.date(year=1970, month=1, day=1)
today = dt.date(year.now,month=now.month,day=now.day)
time_left_for_newyear = today - old
print('Time passed for new year: ', time_left_for_newyear)

# Think, what  can you use the datetime module for? Examples:
# - Time series analysis
how to do time series analysis with datetime
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 