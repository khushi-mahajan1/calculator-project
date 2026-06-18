# calculator 

def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    if b==0:
        return"Error: Cannot divide by zero"
    return a/b
def Modulus(a,b):
    return a%b
def Power(a,b):
    return a**b
while True:
    print("1. Addition")
    print("2.Subtraction")
    print("3.Mutliplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Exit")
    choice =input("Enter your choice:")
    if choice=="7":
        print("Thank you for using calculator!")
        break
    num1=float(input("enter the number 1:"))
    num2=float(input("enter the number 2:"))
    if choice=="1":
       print("Result:",Add(num1,num2))
    elif choice=="2":
       print("Result:",Subtract(num1,num2))
    elif choice=="3":
      print("Result:",Multiply(num1,num2))
    elif choice=="4":
       print("Result:",Divide(num1,num2))
    elif choice=="5":
       print("Result:",Modulus(num1,num2))
    elif choice=="6":
       print("Result:",Power(num1,num2))
    else:
       print("Invalid Choice")
