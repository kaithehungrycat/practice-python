#! python3
#phoneAndMail.py - Search for phone numbers and email addresses

import pyperclip
import re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  #numer kierunkowy
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4})
(\s*(ext|x|ext.)\s*\d{2-5})?
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)



a = str(pyperclip.paste())
phoneNum = []
matches = []

for groups in phoneRegex.findall(a):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[7] != '':
        phoneNum += groups[7]
    matches.append(phoneNum)
for groups in emailRegex.findall(a):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Coppied to clippboard:')
    print('\n'.join(matches))
else:
    print('no num or email found')
