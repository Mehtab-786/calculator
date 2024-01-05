def add(n1,n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2


def divide(n1,n2):
    return n1/n2


def multiply(n1,n2):
    return n1 * n2


operations = {"+":add ,"-":subtract ,"/":divide ,"*":multiply}

num1 = int(input("enter your first number :"))
num2 = int(input("enter your second number :"))

for i in operations: # for showing the options to user
    print(i)

symbol = input("Pick an operation from the line above : ")
calculation = operations[symbol]
answer = calculation(num1,num2)

print(f"{num1} {symbol} {num2} = {answer}") # used f-string