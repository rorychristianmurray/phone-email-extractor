!# python3
# phoneAndEmail.py - FInds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compiler(r'''(
  (\d{3}|\(\d{3}\))? # area code
  (\s|-|\.)? # separator
  (\d{3}) # first three digits
  (\s|-|\.) # separator
  (\d{4}) # last 4 digits
  (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

# create email regex

emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+ # username
  @ # connector
  [a-zA-Z0-9.-]+ # domain name
  (\.[a-zA-Z]{2,4}) # dot something
)''', re.VERBOSE)

# find matches in clipboard text

# copy results to clipboard


