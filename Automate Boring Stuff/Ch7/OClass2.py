import re
#
# noNewlineRegex = re.compile('.*')
# a = noNewlineRegex.search('What can I do. \n When I can\'t do anything. \n thx God I still ahve whiskey.').group(0)
#
# print(a)
#
# noNewlineRegex = re.compile('.*', re.DOTALL)
# b = noNewlineRegex.search('What can I do. \n When I can\'t do anything. \n thx God I still ahve whiskey.').group(0)
#
# print(b)

# rob = re.compile(r'robocop', re.I) #OR re.IGNORECASE
# a = rob.findall('Robocop roboCop RoboCOPROBOCOP ROBOCOP robocoP')
# print(a)

# namesRegex = re.compile(r'Agent \w+')
# a = namesRegex.sub('CENSORED', 'Agent has one huuuuge problem with his ID. Agent needs new ID!')
# print(a)

# agentNameReg = re.compile(r'Agent (\w\w)\w*')
# a = agentNameReg.sub(r'\1***','Agent ALicja Agent Karolina Agent Karol and all other staff members')
# print(a)

# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?  #numer kierunkowy
# (\s|-|\.)?
# \d{3}
# (\s|-|\.)?
# \d{4}
# (\s*(ext|x|ext.)\s*\d{2-5})?
# )''', re.VERBOSE)

#BITWISEOPERATOR