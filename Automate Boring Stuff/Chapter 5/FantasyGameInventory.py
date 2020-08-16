inventory = {'Arrow': 12, 'Gold coin': 42, 'Rope': 1, 'Firetorch': 6, 'Dagger': 1}
dragonloot = ['Gold coin', 'Dagger', 'Gold coin', 'Ruby', 'Gold coin']


def displayInv(inventory):
    print('Inventory:')
    total = 0
    for item, quantity in inventory.items():
        print(str(quantity) + ' ' + item)
        total += quantity
    print('Total number of items in inv : ' + str(total))


print(displayInv(inventory))  # end of first part


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inventory, dragonloot)
displayInv(inventory)
