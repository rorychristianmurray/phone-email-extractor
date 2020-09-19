# Date Detection

# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

import pyperclip, re

# write regex

dateRegex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9][0-9][0-9])')

# read clipboard

text='hello world 31/01/1999 05/09/1716 bin 20/01/3000 31/06/1975 30/06/1975 29/02/1975 14/02/1975'

# text = str(pyperclip.paste())

# store strings in variables

dates = []

for group in dateRegex.findall(text):
  # check if valid
  d = group
  day = group[0]
  month = group[1]
  year = group[2]
  # dates.append(d)
  # if month 4, 6, 9, 11 - 30 days
  if month == '04' and day != '31':
    print(f'd : {d}')
  elif month == '06' and day != '31':
    print(f'd : {d}')
  elif month == '09' and day != '31':
    print(f'd : {d}')
  elif month == '11' and day != '31':
    print(f'd : {d}')
  elif month == '02':
    if int(day) < 29:
      if int(year) %4 == 0:
        if int(year) % 100 == 0:
          print(f'd : {d}')

# print(f'dates : {dates}')
# get returned matches
# they should be grouped

# check validity

# return string
