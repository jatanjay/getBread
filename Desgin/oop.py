# %%
class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    """
    2/3/2024
    when to use class variable
    like 

    Employee.VAR
    v/s 
    self.VAR


    self.VAR can be changed by each instance
    Employee.VAR cannot be chnaged by instances

    see raise_amout v/s num_of_employee
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_employees)

emp1 = Employee("Jatan", "Pandya", 50000)
emp2 = Employee("Jatan", "Pandya", 500)

emp1.raise_amount = 1.50
print(emp1.raise_amount)
emp1.apply_raise()
print(emp1.pay)
print(Employee.raise_amount)

# %%
