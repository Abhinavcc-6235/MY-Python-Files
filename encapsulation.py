class Bankaccount:
    def __init__(self,owner_name,bank_balance,account_type):
        self.owner_name=owner_name
        self.__bank_balance=bank_balance
        self._account_type=account_type

    #to get privte proprty
    @property
    def bank_balance(self):
        return self.__bank_balance  
    @property
    def account_type(self):
        return self._account_type
    
    @bank_balance.setter
    def bank_balance(self,depposit_amt):
        if depposit_amt<=0:
            raise ValueError ("deposit amount cant be zero or negative value")
        self.__bank_balance=self.__bank_balance+depposit_amt

    @account_type.setter
    def account_type(self,account_type):
        if account_type == "":
         raise ValueError("Account type cannot be empty")
        self._account_type=account_type
               
     
bank=Bankaccount('ABC',1200,'current')
print(bank.bank_balance)  
print(bank.account_type)   
#syntax: class setter function=new value
bank.bank_balance=123
print('bank balance is =',bank.bank_balance)
print('account type is:',bank.account_type)

print('**********************************')

# to update the private atribute

class Employee:
    def __init__(self,employee_name,department,salary):
        self.employee_name=employee_name
        self._department=department
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,dep_amt):
        if dep_amt<=0:
            raise ValueError("deposit amount can't be zero or negative value")
        self.__salary = dep_amt

class Manager(Employee):
    def display_details(self):
       print('employee name:',self.employee_name)
       print('department:',self._department)

mng_dtail=Manager('Abhinav','data science',1200)
mng_dtail.display_details()
print('current salary:',mng_dtail.salary )
mng_dtail.salary = 1234
print('updated salary:',mng_dtail.salary)
print('************************************')

class Vehicle:
    def __init__(self,vehicle_name, rental_type, rental_price):
        self.vehicle_name=vehicle_name
        self._rental_type=rental_type
        self.__rental_price=rental_price
    @property
    def rental_price(self):
        return self.__rental_price
    @rental_price.setter
    def rental_price(self,price):
        if price<=0:
            return ValueError('rental price can not be zero or negative')
        self.__rental_price=price
        
    def display_details(self):
        print('vehicle name:',self.vehicle_name) 
        print('rental type:',self._rental_type)


class Car(Vehicle):
    def calculate_rent(self,days):
        self.days=days
        self.rent_calculated=self.rental_price*self.days

        return self.rent_calculated

    def display_details(self):
        print('vehicle name:',self.vehicle_name) 
        print('rental type:',self._rental_type)
        print('rental price car :',self.rent_calculated)

class Bike(Vehicle):
    def calculate_rent(self,days):
        self.days=days
        self.bike_rent=self.rental_price*self.days
        return self.bike_rent

    def display_details(self):
        print('vehicle name:',self.vehicle_name) 
        print('rental type:',self._rental_type)
        print('rental price :',self.rental_price)


car=Car('toyota','4weel',2000)
print('vehicle name:',car.vehicle_name)
print('rental type:',car._rental_type)
print('Rental cost for 3 days=', car.calculate_rent(3))
bike=Bike('pulasr','2weeler',800)
print('vehicle name:',bike.vehicle_name)
print('Rental type:',bike._rental_type)
print('bike rental cost for 3 days=', bike.calculate_rent(3)) 

car.rental_price=45577
print('updted price for car=',car.rental_price)





       
                  

  





