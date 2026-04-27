class Employee:
    language = "Py" # This is a class attribute
    salary = 1400000

    def getinfo(self):
        print(f"The lanuage is {self.language}. The salary is {self.salary}")

Patu = Employee()
Patu.language = "Jawa" # This is an instance attribute
Patu.getinfo()
print(Patu.language, Patu.salary)