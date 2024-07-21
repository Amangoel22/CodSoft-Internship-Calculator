#Creating a calculator (TASK-2)

print("\n---WELCOME TO THE CALCULATOR---\n")
calc=True

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

while (calc==True):
    user = input("\nEnter the operation to be performed(+,-,*,/) (Enter exit to exit application):")
    if user=="+":
        c=a+b
        print("Sum of the above two numbers is:",c)
        a=c
    elif user=="-":
        c=a-b
        print("Subtraction of the above two numbers is:",c)
        a = c
    elif user=="*":
        c=a*b
        print("Multiplication of the above two numbers is:",c)
        a=c
    elif user=="/":
        if b != 0:
            c=a/b
            print("Division of the above two numbers is:",c)
            a = c
        else:
            print("Error: Division by zero.")
    elif user=="exit":
        calc=False
        print("Thank you for using Calculator.")
    else:
        print("Please choose a valid operator.")

    if calc:
        b=int(input("\nEnter the next number:"))


