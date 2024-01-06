def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {"+": add, "-": subtract, "/": divide, "*": multiply}

num1 = int(input("enter your first number :"))
num2 = int(input("enter your second number :"))

for i in operations:  # for showing the options to user
    print(i)

symbol = input("Pick an operation from the line above : ")
calculation = operations[symbol]
answer = calculation(num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")  # used f-string

calculate_further = False

while not calculate_further:
    if input("Do you want to calculate further : ") == "yes":
        another_operation = input("pick another operation :")
        next_number = int(input("enter next number :"))
        num = answer

        calculate = operations[another_operation]
        answer = calculate(num, next_number)
        print(f"{num} {another_operation} {next_number} = {answer}")
    else:
        calculate_further = True



