#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save': # If the first command line argument (which will always be at index 1 of the sys.argv list) is 'save'
        mcbShelf[sys.argv[2]] = pyperclip.paste() #  the second command line argument is the keyword for the current content of the clipboard.
    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf.keys():
        mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()