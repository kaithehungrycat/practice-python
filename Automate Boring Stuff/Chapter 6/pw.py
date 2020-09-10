#! python3
#pw.py - niebezpieczny program menadzer hasel

passwords = {'login':'password','qwerq':'kukaracza', 'abc':'cba' }

import sys, pyperclip
if len(sys.argv)>2:
    print('used pw.py [account] - coppied password of chosen account')
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password to account ' + account + 'was copied')
else:
    print('There is no account such as' + account)