class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_rasie(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "Employee", 60000)


print(emp1 + emp2)
print(len(emp1))
