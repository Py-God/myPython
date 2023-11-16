import shelve
shelfFile = shelve.open('mydata')       # shelve value stored in shelveFile
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats                # storing the list in shelfFile as a value associated with key 'cats', like in a dictionary
shelfFile.close()
