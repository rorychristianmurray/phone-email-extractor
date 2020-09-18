import re

numberCommaRegex = re.compile(r'(\d{1,3}\D)(\,\d{3})*')
# numberCommaRegex = re.compile(r'(\d{1,3})(\,)?')

ft = numberCommaRegex.search('hello 1,420,987')
f1 = numberCommaRegex.search('42')
f2 = numberCommaRegex.search('1,234')
f3 = numberCommaRegex.search('6,368,745')
f4 = numberCommaRegex.search('1234')

fArr = [ft, f1, f2, f3, f4]

for item in fArr:
  if item:
    print(item)

# print(f'ft {ft}')
# print(f'f1 {f1}')
# print(f'f2 {f2}')
# print(f'f3 {f3}')
# print(f'f4 {f4}')



# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# but not the following:

# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized)

# watanabeRegex = re.compile(r'([A-Z][A-Za-z]*/s)(Watanabe)')
watanabeRegex = re.compile(r'([A-Z][a-z]*\s)(Watanabe)')

w1 = watanabeRegex.search('Haruto Watanabe')
w2 = watanabeRegex.search('Alice Watanabe')
w3 = watanabeRegex.search('RoboCop Watanabe')
w4 = watanabeRegex.search('haruto Watanabe')
w5 = watanabeRegex.search('Watanabe')
w6 = watanabeRegex.search('Haruto watanabe')

print(f'w1 {w1}')
print(f'w2 {w2}')
print(f'w3 {w3}')
print(f'w4 {w4}')
print(f'w5 {w5}')
print(f'w6 {w6}')

