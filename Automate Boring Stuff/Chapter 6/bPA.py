#! python3
#bulletPointAdder.py - add * to all text copied in clipboard
import pyperclip
text = pyperclip.paste()

#split of specific rows

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
