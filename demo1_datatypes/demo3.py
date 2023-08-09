colors=["red","green","orange","black"]
#mutable
print(colors)
print(len(colors))
print(type(colors))

print(colors[2])

#append yellow to the list
colors.append("yellow")
print(colors)

#remove green from the list
colors.remove("green")
print(colors)
#insert pink at index 1
colors.insert(0,"pink")

print(colors)

#remove value at index 0
colors.remove(colors[0])
print(colors)

#tuple
#tuple will be faster
#immutable
signal=("red","yellow","green")

print(signal[0])

check=True
