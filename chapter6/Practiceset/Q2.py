# Write a program to find out whether a student has passed or failed it. it requires total of 40% and 33% in each subject to pass. Assume three subjects

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

# Check for total percentage
total_percentage = (m1 + m2 + m3)/300

if(total_percentage>=40):
    print("You are passed.")

else:
    print("You are failed, Try again next year.")
