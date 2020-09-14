import re

#
# xmasRegex = re.compile(r'\d+\s\w+')
# oxR = xmasRegex.findall('12 lolo, 13 yup, 14 hahaha, 1 go_funk_yourself')
# print(oxR)
#
# # vowRegex = re.compile(r'[^aeiouAEIOU]')
# # papaya = vowRegex.findall('RoboCop eats food for kids. Damn FOOD FOR KIDS!')
# # print(papaya)
# #
# # #range we can declare with [a-zA-Z0-9]
# WSIN = re.compile(r'^\d+$')
# a = WSIN.search('1123456781323412')
#
# print(a)

# atRegex = re.compile(r'.ba')
# beeee = atRegex.findall('Baba baobaba baby byba uabeba')
# print(beeee)

# dot and star '.' & '*'

# nameRegex = re.compile(r'Name: (.*) Surname: (.*)')
# mo = nameRegex.search('Name: Krzysztof Surname: Papaya')
# ma = nameRegex.findall('Name: Krzysztof Surname: Papaya')
# a = mo.group(0)
# print(a)
# print(ma)

whoIsGreesdyRegex = re.compile(r'<.*?>')
mo = whoIsGreesdyRegex.search('<this is it>you filthy motherhugger>')

wellIamGreedy = re.compile(r'<.*>')
ma = wellIamGreedy.search('<this is it>you filthy motherhugger>')

print(mo)
print(ma)