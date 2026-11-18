# #**************controlflow statements*********************
# #*********checking wether a number is bigger than 50****
# #******************************************************
# #number_int > 50 #the number enterd is bigger than 50
#  # #number_int > 50 #the number enterd is lesser than 50
number=input('Please enter a number:')   #convert input as number
number_int=int(number) 
if(number_int>50):
    print('the number enterd is bigger than 50')
if(number_int<50):
    print('the number enterd is lesser than 50')
    #********************************
    #******** else if statement*******
    #********************************
    if(number_int>50):
        print('the number enterd is bigger than 50') #print the statement if the number is bigger than 50
    else:                                             #if else statement is used to check the condition if the number is not bigger than 50 then it will print the below statement
        print('the number enterd is smaller than 50')  #print the statement if the number is smaller than 50
#****************************************
#find odd or even number
num=input('Please enter a number:')   #convert input as number
number=int(num)  
if((number%2)==0):
    print('the number enterd is even')
else:
    print('the number enterd is odd')


    #********************************
temp=input('Please enter a temperature in celcius:')   #convert input as number
temp=float(temp)
#>=35 : very hot
#25-35 : warm
#15-25 : cool
#<15 : freezing
if(temp>=35):
    print('the temperature is very hot')
else:
    if(temp>=25):
        print('the temperature is warm')
    else:
        if(temp>=15):
            print('the temperature is cool')
        else:
            print('the temperature is freezing')
#*******elseif**********  
if(temp>=35):                   
    print('temprature is hot')  
elif(temp>=25):
     print('temprature is warm')
elif(temp>=15):
    print('temprature is cool')
else:
    print('temprature is freezing') 

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
for i in range(1,50,2):
    print(i)
# print all odd numbers between 20&50
for i in range(21,50,1):
 print(i)
 #***************WHILE LOOP*************
 #**************************************
num=1
while(num<10):
    print(num)
    num= num  + 1
print('end of while loop')
#print all odd numbers <50
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
#logical operator in control flow statements
age=int((input('enter your age')))    
valid_id=int((input('do you have valid id (Y/N)'))) 
if (valid_id=='Y'):
    valid_id= True
else:
    valid_id=False
#verify the eligibility to vote
print('we are checking your elgibility')
if(age>=18):
    if(valid_id):
        print('you are eligeble to vote')    
else:
    print('you are not elgible to vote')

