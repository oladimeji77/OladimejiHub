Items = ['ola', 'deji', 250, 'folawe', 'akin']
Items2 = ['dami', 'ufuoma', '430ad', 550]


print(Items)  #the entie Items list
print(len(Items))  #lenght of list
print(Items[3])  #
print(Items[1:3])
Items.append(700)
print(Items)
print(Items[-1])
Items.insert(0, "Enitan")
print(Items)
print(Items.pop())
print(Items)
print(Items.pop(4))
print(Items)
all_items = [Items, Items2]
print(all_items)
print(all_items[1][-1])