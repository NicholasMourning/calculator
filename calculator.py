
def addition (x,y):
    return x + y

def subtraction (x,y):
    return x - y

def multiplication (x,y):
    return x * y

def division (x,y):
    return x/y

while True:
    calcuation = input("What do you want to calculate: addition / subtraction / multiplication / division ")
    number1 = int(input("What is your first number "))
    number2 = int(input("What is your second number "))

    if(calcuation == "addition"):
        print(addition(number1,number2))
        break

    elif(calcuation == "subraction"):
        print(subtraction(number1,number2))
        break

    elif(calcuation == "multiplication"):
        print(multiplication(number1,number2))
        break
    
    elif(calcuation == "division"):
        print(division(number1,number2))
        break