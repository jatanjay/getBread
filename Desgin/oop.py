import datetime


class Employee:
    raise_amt = 1.04
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



    2/3/2023
    see decorators.py for info about first class citizen fx,
    high order fx, and decorators


    A. classmethods
    help change class attributes (see raise_amt)
    takes cls as first arg, (not self)

    1. A class method is a method that is bound to the class and not the object of the class.
    2. They have the access to the state of the class as it takes a class parameter that points
        to the class and not the object instance.
    3. It can modify a class state that would apply across all the instances of the class.
        For example, it can modify a class variable that will be applicable to all the instances.


    B. staticmethods
    1. not really usefull for inner workings for class,
        can be put into static methods, cz it makes logical sense to be put
    2. Doesn't take any self/cls
    3. can't change state of class (since doesn't tkae cls/self)


    C. Inheritance:
    1. Helpfull isinstance(), issubclass()

    D. Dunder Methods:

    1. repr - for devs
    2. str - readable obj
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"

    def __str__(self):
        return f"{self.fullname()},{self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Del")
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rm_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


emp1 = Developer("Jatan", "Pandya", 50000, "Python")
emp2 = Developer("Jatan", "Pandya", 500, "Java")
