# # #regular expressions
# #
import re
#
#phoneNumRegex = re.compile(r'\d{3}-\d{4}')
#phoneNumRegex = re.compile(r'((\(\d{3}\))? (\d{3}-\d{4}))')#()? / (\(\))
#mo = phoneNumRegex.search('My phone number is (342) 333-1293 or (321) 222-2314. Please call me if needed.')

#print(mo.group())
#print(mo) #mo.group przy .search
# # heroRegex = re.compile(r'Batman|Tina Fey')
# # mo1 = heroRegex.search('Batman i Tina Fey')
# # print(mo1.group())
# #
# # batRegex = re.compile(r'Bat(man|mobile|(copter)?|bat)')
# # mo = batRegex.search('Batcopter fall from the sky and Batmobile burned dawn')
# # print(mo.group())
#
# #(ha){3,5}
# haRegex = re.compile(r'(ha){3,5}?') #? changes target from max to minimum value
# mo1 = haRegex.search('hahahahahahahaha')
# print(mo1.group())

#find all vs search

#phoneNumRegex = re.compile(r'\d{3}-\d{4}')
#phoneNumRegex = re.compile(r'((\(\d{3}\))? (\d{3}-\d{4}))')#()? / (\(\))
#mo = phoneNumRegex.search('My phone number is (342) 333-1293 or (321) 222-2314. Please call me if needed.')

#print(mo.group())
#print(mo) #mo.group przy .search