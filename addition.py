num1 = int(input("enter num1 "))
num2 = int(input("enter num2 "))

def add(num1, num2):
    addition = num1 + num2
    if num1 == num2:
        print("do not print eqaul numbers")
    else:
        return addition


print(add(num1, num2))
