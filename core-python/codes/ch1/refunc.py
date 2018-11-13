import re

m = re.match("foo", "food on the table")
if m is not None:
    print(m.group())
# foo

m = re.match("foo", "seafood")
if m is not None:
    print(m.group())
else:
    print("match failed")
# match failed

m = re.search("foo", "seafood")
if m is not None:
    print(m.group())
# foo


m = re.match('ab', 'ab')
print(m.group())
print(m.groups())


m = re.match('(a(b))', 'ab')
print(m.group())
print(m.groups())

m = re.match('((a)(b))', 'ab')
print(m.group())
print(m.groups())

m = re.search(r'''
    \((\d{3})\)
    [ ]
    (\d{3})
    -
    (\d{4})
    ''', '(800) 555-1212', re.VERBOSE)

print(m.groups())
