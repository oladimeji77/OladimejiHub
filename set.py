#Set

friends = {"deji", "folawe", "Eni"}

abroad = {"Nisham", "deji"}

All_friends = friends.union(abroad)
print(All_friends)
local_friends = friends.difference(abroad)
print(local_friends)
other_friends = abroad.difference(friends)
print(other_friends)
common = friends.intersection(abroad) 
print(common)


#Empty set is set()
