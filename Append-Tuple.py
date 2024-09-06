x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)

print(y)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)