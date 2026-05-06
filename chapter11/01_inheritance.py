# Single Inheritance

class Employee:
    company = "ITC"
    name = "Patu"
    salary = 100000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmmer(Employee):
    company = "ITC Infotech "
    language = "Py"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language.")

a = Employee()
b = Programmmer()

print(a.company,a.name)