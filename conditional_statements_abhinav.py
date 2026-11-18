#1
number=input('Please enter a number:')   #convert input as number
number=int(number)
if(number > 0):
    print('the number entered is positive')
elif(number < 0):
    print('the number entered is negative')
#2

age=input('Please enter your age:')   #convert input as number
age=int(age)
if(age>18):
    print('you are eligible for voting')
elif(age<=18):
    print('you are not eligible for voting')    

#3
num=input('please enter a number:')
num=int(num)
if(num%2==0):
    print('the number enterd is even')
else:
    print('the number enterd is odd')

#4
password= 'clear'
user_password=input('please enter the password:')  
if(user_password==password):
    print('Access granted')
else:
    print('Access denied')

#5
num1=input('please enter first number:')
num2=input('please enter second number:')
if(num1>num2):
    print('the first number is greater')
elif(num2>num1):
    print('the second number is greater')
else:
    print('both numbers are equal') 
#6
marks=input('please enter your marks out of 100:')
marks=int(marks)
if(marks>=90):
    print('Grade A')
elif(marks>=80):
    print('Grade B')
elif(marks>=70):
    print('Grade C')
elif(marks>=60):
    print('Grade D')
elif(marks>=50):
    print('Grade E')
else:
    print('Grade Fail')  

#7
num1=input('please enter first number:')
num2=input('please enter second number:')
num3=input('please enter third number:')     
if(num1>num2 and num1>num3):
    print('largest number is :',num1)
elif(num2>num1 and num2>num3):
    print('largest number is :',num2)
else:
    print('largest number is:',num3)

#8
colour=input('please enter a traffic colour:')
if(colour=='red'):
    print('stop')
elif(colour=='yellow'):
    print('Get ready')
elif(colour=='Green'):
    print('Go')
else:
    print('Invalid colour')

# #10
account_balance=10000
print('account balance is:',account_balance)
withdraw_amount=input('please enter the amount you want to withdraw:')
withdraw_amount=float(withdraw_amount)
if(withdraw_amount>0 and withdraw_amount % 100 == 0 and account_balance>withdraw_amount):
    remaing_balance=account_balance-withdraw_amount
    print('transaction succesful')
    print('remaining balance',remaing_balance)
else:
    print('transaction failed')

#**********************************
#**********ITERATIVE STATEMENTS****

#iterative statements are used to repeat a block of code multiple times

# for loop : used when no of iterations is known
#while loop : used when no of iteration is not known,stopping condition is known

#print your name 10 times
for i in range(10):       #we are giving number of interations as 10
    print(i,': Abhinav')      #iterative (repeated) task

for i in range(0,10,2):   #start:stop:step
    print(i,': Abhinav')      #iterative (repeated) task
for i in range(3,10,3):
    print(i,'abhinav')  
    #range(start:end:step) # step isnot mentioned then default step is 1
 #giving step as negative value
for i in range(10,3,-1):
    print(i,':abhinav')
# print all odd numbers less than 50
# for i in range(1,50,2):
#     print(i)
# print all odd numbers between 20&50
for i in range(21,50,1):
 print(i)
 #***************WHILE LOOP*************
 #**************************************
# num=1
# while(num<10):
#     print(num)
#     num= num + 1
# print('end of while loop')
# print all odd numbers <50
print('all odd numbers lessthan 50')
num=1
while(num<50):
    print(num,end=',')
    num=num+2


#print all odd numbers between 20&50
print('\n''odd numbers between 20&50')
num=21
while(num<50):
    print(num,end=',')
    num=num+2
   
