import os

# myFiles = ['accounts.txt', 'bills.docx', 'event.xls']
# for filename in myFiles:
#     print(os.path.join('C:\\files', filename))
# os.chdir('C:\\')
# a = os.getcwd()
# print(a)
# os.makedirs('D:\\Project\\4fun')

#os.path.asbpath(path) #show absolute path of xyz
#os.path.relpath(path, beggining) #converter
#os.path.isabs(path) #boolean

#os.path.getsize(filename) #file size
#os.listdir(path) #gives list of files in path

# helloFile = open('D:\\hello.txt')
# helloContent = helloFile.readlines() #readlines() or read()
# print(helloContent)
# testFile = open('D:\\test.txt', 'a')
# testFile.write('lol nope?')
# testFile.close()
# testFile = open('D:\\test.txt')
# testABC = testFile.read()
# print(testABC)

# import shelve
#
# shelvefile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelvefile['cats'] = cats
# shelvefile.close()
#
# shelvefile = shelve.open('mydata')
# a = list(shelvefile.keys())
# b = list(shelvefile.values())
#
# print(a)
# print(b)
# import pprint
# cats = [{'abc' : 'lool', 'def' : 'lool2'}, {'name' : 'get lost', 'surname' : 'da fuq'}]
# a = pprint.pformat(cats)
# print(a)
# fileObj = open('C:\\PycharmProjects\\practice-python\\Automate Boring Stuff\\Ch8\\mcats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()
#
# import mcats
# print(mcats.cats[0]['abc'])