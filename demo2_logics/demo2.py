numbers = [78, 98, 54, 12, 65, 4, 5, 25, 29, 33, 40]

print(len(numbers))

""" for loop"""
# print only the numbers less than or equal to 50
for i in range(0, len(numbers)):
    if numbers[i]<=50:
        print(numbers[i])

"""advance for loop"""
for num in numbers:
    if num<=50:
        print(num)


print("end of the code")