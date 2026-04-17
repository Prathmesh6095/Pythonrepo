# Write a program using functions to find ggreatest of three numbers.
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
    
print(greatest(a, b, c))