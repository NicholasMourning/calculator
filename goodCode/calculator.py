
from calculation import Calculations

# Creating an instance of the Calcuations class
calculation = Calculations()

## Main function to execute the calculator
def main():
    while True:
        calculate = input("What do you want to calculate: addition / subtraction / multiplication / division ")
        while True:
            try:
                number1 = int(input("What is your first number: "))
                break
            except ValueError:
                print("Please enter a valid number")
        
        while True:
            try:
                number2 = int(input("What is your second number: "))
                break
            except ValueError:
                print("Please enter a valid number")
        
        if(calculate == "addition"):
            print(calculation.addition(number1,number2))
            break

        elif(calculate == "subtraction"):
            print(calculation.subtraction(number1,number2))
            break

        elif(calculate == "multiplication"):
            print(calculation.multiplication(number1,number2))
            break
        
        elif(calculate == "division"):
            print(calculation.division(number1,number2))
            break

        else:
            print("calculcation inputed wrong")

if __name__=="__main__":
    main()