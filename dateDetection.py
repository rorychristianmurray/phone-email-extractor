# Date Detection

# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

import pyperclip, re

# write regex

dateRegex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9][0-9][0-9])')

d1 = dateRegex.search('31/01/1999')
d2 = dateRegex.search('12/12/2999')
d3 = dateRegex.search('05/09/1716')
d4 = dateRegex.search('19/50/1999')
d5 = dateRegex.search('41/01/1999')
d6 = dateRegex.search('20/01/3000')

print(f'd1 {d1}')
print(f'd2 {d2}')
print(f'd3 {d3}')
print(f'd4 {d4}')
print(f'd5 {d5}')
print(f'd6 {d6}')

# read clipboard



# store strings in variables

# check validity

# return string
