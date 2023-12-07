"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    def get_salary(self):
        pass

class MonthlySalary(Contract):
    def __init__(self, salary):
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    def __str__(self):
        return f"a monthly salary of {self.salary}"
    
class HourlyContract(Contract):
    def __init__(self, number_of_hours, hourly_rate):
        self.number_of_hours = number_of_hours
        self.hourly_rate = hourly_rate
    
    def get_salary(self):
        return self.number_of_hours * self.hourly_rate
    
    def __str__(self):
        return f"a contract of {self.number_of_hours} hours at {self.hourly_rate}/hour"

class Commission:
    def get_commission(self):
        pass

class Bonus(Commission):

    def __init__(self, bonus):
        self.bonus = bonus

    def get_commission(self):
        return self.bonus
    
    def __str__(self):
        return f"a bonus commission of {self.bonus}"

class ContractsCommission(Commission):
    def __init__(self, number_of_contracts, contract_commission):
        self.number_of_contracts = number_of_contracts
        self.contract_commission = contract_commission

    def get_commission(self):
        return self.number_of_contracts * self.contract_commission
    
    def __str__(self):
        return f"a commission for {self.number_of_contracts} contract(s) at {self.contract_commission}/contract"

class Employee:
    def __init__(self, name, contract, commssion=None):
        self.name = name
        self.contract = contract
        self.commission = commssion

    def get_pay(self):
        pay = self.contract.get_salary()
        if self.commission:
            pay += self.commission.get_commission()
        return pay

    def __str__(self):
        rep = f"{self.name} works on {self.contract}"
        if self.commission:
            rep+= f" and receives {self.commission}"
        rep += f". Their total pay is {self.get_pay()}."
        return rep

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractsCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(150, 25), ContractsCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), Bonus(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(120, 30), Bonus(600))
