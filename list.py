list_1 = list([2, 4, 'June', 'Hello', 'C', 'June'])
print(dir(list_1))


print(list_1.count('June'))
list_1.extend([5, 6, 7])
c = list_1.copy()
print(c, type(c))
print(list_1.reverse())

dic = {
    "name": "Dorji",
    "age": 23
}


list_1 = list([2, 4, 'June', 'Hello', 'C', 'June'])
list_2 = ['Monday', 'Flowers', 45, 90, 4.3]
# print(list_2)

# """ modify list """
# list_2.append('Hey')
# list_2[0] = 'January'
# print(list_2)
# print(list_2[1])
# print(list_2[1:4])

# """ list inside list """
list_3 = [list_1, list_2]
print(list_3)
print(list_3[1])
print(list_3[1][0])


# """ List comprehensions - a shorter syntax to create a new list"""
# """ Syntax: [expression for item in iterable if condition == True] """
newlist = [x for x in range(5,100) if x % 5 == 0]
print(newlist)
