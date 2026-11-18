class Person():
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def display_details(self):
        print('employee name:',(self.name),'employee age:',(self.age))

class Employee(Person):
    def __init__(self, name, age,salary,emp_id,joining_date):
        super().__init__(name, age)
        self.salary=salary
        self.emp_id=emp_id
        self.joining_date=joining_date

    def display_details(self):
        print('employee name:',(self.name),'employee age:',(self.age),'emp_id:',(self.emp_id),'joining_date:',(self.joining_date))
class Father(Person):
    def __init__(self, name, age,no_child):
        super().__init__(name, age)
        self.age=age
        self.no_child=no_child
    def display_details(self):
        print('employee name:',(self.name),'employee age:',(self.age),'num_ofchild:',(self.no_child))   
class Son(Person):
    def __init__(self, name, age,father_name):
        super().__init__(name, age)
        self.name=name
        self.age=age
        self.father_name=father_name
    def dislpay_details(self):
        print('employee name:',(self.name),'employee age:',(self.age),'father_name:',(self.father_name))        
class Husband(Person):
    def __init__(self, name, age,wife_name,date_of_marriage):
        super().__init__(name, age)
        self.name=name
        self.age=age
        self.wife_name=wife_name
        self.date_of_marriage=date_of_marriage
    def display_details(self):
        print('employee name:',(self.name),'employee age:',(self.age),'wife name:',(self.wife_name),'date_mrg:',(self.date_of_marriage))

person=Person('jhon',35)
person.display_details()
emple=Employee('jhon',34,3444,54,20/5/2024)
emple.display_details()
father=Father('jose',55,2)
father.display_details()
son=Son('nithin',23,'jose')
son.display_details()
hus=Husband('david',29,'maya',(20-5-2000))
hus.display_details()
print('************************************')


class Employee:
    def calculate_salary(self):
     print('calculating employee salary:')
class Fulltimeemolyee(Employee):
    def calculate_salary(self):
        print('full time employee recievs a fixed monthly salary')
class Partimeemolyee(Employee):
    def calculate_salary(self):
        print('part time employee  salary is based on working hours')   
class Freelancer(Employee):
    def calculate_salary(self):
        print('freelancer salary based completed projects')   

Fulltimeemolyee().calculate_salary()
Partimeemolyee().calculate_salary()
Freelancer().calculate_salary()

print('****************************') 



from abc import ABC,abstractmethod



class BankAccount(ABC):

    def __init__(self,account_holder,account_type,balance):
        self.account_holder=account_holder
        self._account_type=account_type
        self.__balance=balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,deposit_amt):
        if deposit_amt<0:
            raise ValueError("balance dosen't allow negative balance")
        self.__balance=deposit_amt
    def deposit(self,amount):
        if amount<=0:
            print('deposit amount must be positive')
            return
        self.balance=self.balance+amount
        print(f'deposit successful:Rs.{amount}')
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawal successful: Rs.{amount}")
        else:
            print("Insufficient balance")

    def display_details(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Account Type: {self._account_type}")
        print(f"Balance: Rs.{self.balance}") 

    @abstractmethod
    def calculate_interest(self):
        pass         
      
    
    

class SavingAccount(BankAccount):

    def __init__(self, account_holder, balance):
        super().__init__(account_holder, "Savings", balance)

    def calculate_interest(self, rate):
        return self.balance * (rate / 100)
    
class CurrentAccount(BankAccount):

    def __init__(self, account_holder, balance):
        super().__init__(account_holder, "Current", balance)

    def calculate_interest(self,rate):
        return    self.balance*(rate/100)
            

ashbi = SavingAccount("Ashbi", 10000)
rahul = CurrentAccount("Rahul", 20000)

ashbi.deposit(5000)
ashbi.withdraw(2000)

rahul.deposit(3000)
rahul.withdraw(5000)
print("\n---------- ACCOUNT DETAILS ----------")
ashbi.display_details()
rahul.display_details() 
print("\n---------- ANNUAL INTEREST ----------")
print(f"Ashbi's Annual Interest: Rs.{ashbi.calculate_interest(5)}")
print(f"Rahul's Annual Interest: Rs.{rahul.calculate_interest(2)}")




                        

