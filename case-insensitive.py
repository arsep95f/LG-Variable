thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() #By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters#
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) 
print(thislist)