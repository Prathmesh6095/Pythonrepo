a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey, You cannot divide by zero!")

else:
    print(f"The Division a/b is {a/b}")