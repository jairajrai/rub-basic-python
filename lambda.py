""" Eg.1 start """
def add(a, b):
    c = a + b
    return c
print(add(10, 4))

add = lambda a, b: a + b
print(add(10, 4))
""" end """

# """ Eg.2 start """
# # Example: Filter even numbers from a list
# n = list(range(10))
# even = filter(lambda x: x % 2 == 0, n)
# print(list(even))
# """ end """