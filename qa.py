# What is the function that creates Regex objects?

.compile()

# Why are raw strings often used when creating Regex objects?

easier than escaping special characters

# What does the search() method return?

It returns a Match object with a group method to return matched text

# How do you get the actual strings that match the pattern from a Match object?

You use the group and groups method

# In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

Group 0 is both groups, group 1 is (\d\d\d) and group 2 is (\d\d\d-\d\d\d\d)

# Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

escape them

# The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

If there are groups in the matches

# What does the | character signify in regular expressions?

pipe signifies or

# What two things does the ? character signify in regular expressions?

the ? char signifies that it's an optional value or itself (the \? char)

# What is the difference between the + and * characters in regular expressions?

+ means match one or more of the pattern type, * means match zero or more of the preceding character

# What is the difference between {3} and {3,5} in regular expressions?
{3} means 3 characts of the pattern type, {3,5} means between 3 to 5

# What do the \d, \w, and \s shorthand character classes signify in regular expressions?

\d is digit types, \w is word types, and \s is non word types such as newlines and spaces

# What do the \D, \W, and \S shorthand character classes signify in regular expressions?

they are the inverse of the lowercase types, i.e. everything BUT those types

# What is the difference between .* and .*??

.* means match anything and .*? means match anything but is optional

# What is the character class syntax to match all numbers and lowercase letters?
[a-z0-9]

# How do you make a regular expression case-insensitive?
You can use an option in the compiler for re.IGNORECASE

# What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

It normally matches anything but a newline. Adding re.DOTALL as the second argument to re.compile() will match all characters including newline

# If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

'XX drummers, XX pipers, five rings, X hens'

# What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

It allows you to tell the compile function to ignore whitespace and comments inside the
regex, in order to make it easier to format complex expressions

# How would you write a regex that matches a number with commas for every three digits? It must match the following:

# '42'
# '1,234'
# '6,368,745'
# but not the following:

# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)

# match up to 3 digits

# match ,3digits one or more times

# group 1

(\d{1,3})

# group 2

(,\d{3})

numberCommaRegex = re.compile(r'(\d{1,3})(,\d{3})')

# How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# but not the following:

# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized)

# group 1
# cap letter
[A-Z]
# unknown length letters
[A-Za-z]*
# space
/s

([A-Z][A-Za-z]*/s)


# group 2
# Watanabe
(Watanabe)

([A-Z][A-Za-z]*/s)(Watanabe)

# How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# but not the following:

# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'

# group 1
(Alice|Bob|Carol)

# group 2
(\seats|\spets|\sthrows)

# group 3
(\sapples.|\scats.|\sbaseballs.)

# case insenstive

re.IGNORECASE

(Alice|Bob|Carol)(\seats|\spets|\sthrows)(\sapples.|\scats.|\sbaseballs.)

# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
