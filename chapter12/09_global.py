a = 89 # Global variable

def fun():
    global a # Now It assigns global variable's value
    a = 3

    print(a)
    

print(a)

fun()