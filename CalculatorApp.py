import prompt_toolkit

def add(x , y):
    return x + y
def subtract(x , y):
    return x - y
def multiply(x , y):
    return x * y
def divide(x ,y):
    if y!=0:
        return x/y
    else:
        return "Eror 1"
while True:
    print("Values:")
    x=int(input())
    y=int(input())
    print("What you'd want me to do with thos values")
    print("a)Add them")
    print("b)Subtract them")
    print("c)Multiply them")
    print("d)Divide them")
    print("Choose:")
    z=input()
    if z=='a':
        print(add(x , y))
    if z=='b':
        print(subtract(x , y))
    if z=='c':
        print(multiply(x , y))
    if z=='d':
        print(divide(x , y))
    print("Do you want to leave the calculator")
    statement = input()
    if statement == "yes":
        break
    else:
        continue