# #********input***********
# from os import name


username =input('please enter your name-') #we wait for the user to enter the value
password=input('please enter your password-')
#username
print('the username you enterd is:',username)
print('the password you enterd is:',password)
print('Data type of', username,type(username))
print('Data type of', password,type(password))
#Always the output from the function input() is of datatype 'string'
#we have to explicity convert into numerical data type of need.
#int(variable_name)#integer
#float(variable_name)#float
age=input(' enter your age-')        #fetching age
height=input('enter your height-')
age=int(age)                        #
height=float(height)
print('the age you enterd is:',age)
print('the height you enterd is:',height)
print('Data type of',age,type(age))
print('Data type of',height,type(height))
#*********self introduction************
name=input('enter your name : ')
place=input('enter your place')
age=input('enter your age')
course=input('enter your course details')
college=input('enter your college')
Date_of_birth=input('enter your date of birth')

print('\nselfintroduction')
print('My name is',name,'iam from',place,'my age is',age,)
print('i gradueted in',course,'from',college)
print('my date of birth is',Date_of_birth)




