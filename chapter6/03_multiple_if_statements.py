a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print(a," is even")
# End of if statement no 1

# if statement no: 2
if(a==0) or (a<0):
    print("Invalid number of age. Please enter right age")
elif(a>=18):
    print("You are above the age of consent.")

else:
    print("You are below the age of consent.")
# End of if statement no 1

print("Execution done....")