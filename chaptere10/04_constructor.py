class Employee:
    language = "Py" # This is a class attribute
    salary = 1400000

    def __init__(self): # dunder methos which's automatically called
        print("I am creating an object.")

    def getinfo(self):
        print(f"The lanuage is {self.language}. The salary is {self.salary}")
   
    @staticmethod # There's no need to get self as argument when it declared as @staticmethod 
    def greet():
        print("Good afternoon!")

Patu = Employee()
Patu.language = "Java" # This is an instance attribute
Patu.getinfo()