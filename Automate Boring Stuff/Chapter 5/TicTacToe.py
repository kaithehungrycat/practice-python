# import pprint
#
# msg = 'Jaki byl ten dzien, co darowal co wzial'
# count = {}
#
# for character in msg:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# pprint.pprint(count)

# theBoard = { 'A': { 'topL' : ' ', 'topM' : ' ', 'topR' : ' '},
#             'B': {'midL' : ' ', 'midM' : ' ', 'midR' : ' '},
#             'C': {'lowL' : ' ', 'lowM' : ' ', 'lowR' : ' '}}
#
# for items in theBoard.items():
#     print(items)

# theBoard = {'topL' : ' ', 'topM' : ' ', 'topR' : ' ',
#             'midL' : ' ', 'midM' : ' ', 'midR' : ' ',
#             'lowL' : ' ', 'lowM' : ' ', 'lowR' : ' '}
#
# def printBoard(board):
#     print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
#     print('_+_+_')
#     print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
#     print('_+_+_')
#     print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])
#
#
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Player move ' + turn + '. Where you will place your sign')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = '0'
#     else:
#         turn = 'X'
#
# printBoard(theBoard)


# allGuests = {'Alicia': {'apples': 5, 'pretzels': 12}, 'Bob': {'sandwich': 3, 'Cookies': 2}, 'Karol': {'cups': 3, 'apple pie': 1}}
# #
# def piknikTotal(quests, item):
#     numberBrought = 0
#     for k, v in allGuests.items():
#         numberBrought = numberBrought + v.get(item, 0)
#     return numberBrought
#
# print('list of products: ')
# print('-Apples          ' + str(piknikTotal(allGuests, 'apples')))
# print('-Cups          ' + str(piknikTotal(allGuests, 'cups')))
# print('-Cookies          ' + str(piknikTotal(allGuests, 'Cookies')))
# print('-Mefedron          ' + str(piknikTotal(allGuests, 'mefedron')))
# print('-Apple pie          ' + str(piknikTotal(allGuests, 'apple pie')))


