# Write a program to find whether a given username is contain less than 10 characters or not.

username = input("Enter username: ")

if(len(username)<10):
    print("Your user name contains letters less than 10;")
else:
    print("All is well")