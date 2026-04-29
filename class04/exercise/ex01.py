# write a class of employee
class Employee:
# class attribute is :
    # base salary
    base_salary = 500    
    # company name
    company_name = "whatever"
    # bonus = 0.25
    bonus = 0.25

# instance attributes are :
    # name
    # sales_count
    def __init__(self, name, sales_count):
        self.name = name
        self.sales_count = sales_count

# write a method that calculates their salary and returns it
#   condition: if sales over 10 --> give bonus multiplier per sales
# base salary is : 500
    def calculate_salary(self):
        salary = self.base_salary
        if (self.sales_count > 10):
            salary = salary + (salary * self.bonus * self.sales_count)
        return salary
        

e1 = Employee("test_name", 15) 
e2 = Employee("test_name2", 9) 
e3 = Employee("test_name3", 20) 
e4 = Employee("test_name4", 5) 

print(f"Employee 2 : ${e2.calculate_salary()}")
print(f"Employee 1 : ${e1.calculate_salary()}")
print(f"Employee 3 : ${e3.calculate_salary()}")
print(f"Employee 4 : ${e4.calculate_salary()}")

# Employee.base_salary = 1000
# print("new base salary to $1000")

# print(f"Employee 1 : ${e1.calculate_salary()}")
# print(f"Employee 2 : ${e2.calculate_salary()}")
