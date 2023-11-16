
def displayInventory(inventory):
    print('inventory:')
    
    itemTotal = 0
    items = 0
    for k, v in inventory.items():
        print(v, k)
        
        items = items + v
    itemTotal = itemTotal + items 
    print('Total number of items: ' + str(itemTotal))

def addToInventory(inventory, addedItems):
    
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)
            
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'gold coin', 'dagger', 'gold coin', 'ruby']
newDict = addToInventory(inv, dragonLoot)



displayInventory(inv)
        
