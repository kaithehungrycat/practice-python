a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([aa for aa in a if aa < 5])

#A list comprehension behaves like this: [output] for [item] in [list] if [filter]
#As you can see there are 4 components in its syntax:
# #output, item, list and filter.
#In the case of Sachin's code [aa for aa in a if aa < 5]:
#output = aa
#item = aa
#list = a
#filter = aa < 5
#What this means is that I'm outputting the variable 'aa' which refers to each item in the list (a).
#Since 'aa' is set to refer to each item in list (a), the output will print the items in list (a). However, I also have a filter specified at the end of the code "if aa < 5".
#This means that only the items in the list (referred to as aa) that are below 5 are printed out.
#It does help if you use labels that are more intuitive in your code. For example instead of naming the list a, I can name the list "number_list":
#number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#My list comprehension will go like this:
#[number for number in number_list if number < 5]
#You will get the same output.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)