a = 50
# print(f"Training with cst {a}")

# print("Training")
# print("RUB Branch")

stu = 'hello'
age = 30
hight=152.4

# print(f"stu: {stu} data type: {type(stu)}")
# print(f"stu: {age} data type: {type(age)}")
# print(f"stu: {hight} data type: {type(hight)}")

for item in range(100):
    # print("hellow")
    if item == 5:
        break
    
name = 'the kuensel online'
# print(name.title())
print(name.upper())
print(len(name))


def add_value():
    a = 5
    b = 4
    return a + b

def subtract():
    a = 5
    b = 4
    return a - b
    
# print(add_value())
# print(dir())
# print(dir(__builtins__))

# help(len)

from workwithmodue import add_value, sub_value
a = int(input("Enter Val for a: "))
b = int(input("Enter Val for b: "))

c = add_value(a, b)
d = sub_value(a, b)

print(f"value of add: {c}")
print(f"value of sub: {d}")