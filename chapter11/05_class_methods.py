class Employee:
    a = 1
    @classmethod # Class methos is a method where you can access class attribute directly
    def show(cls):
        print(f" The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

