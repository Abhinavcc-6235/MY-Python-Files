#function to add 2 numbers
# def display_sum(num1,num2):
#     sum=num1+num2
#     print('the sum of',num1,'and',num2,'is',sum)

# a function will have
# function name: manditory
# input(s)
# body of the function(what the function is actually does):mandatory
# output  
# #while we define input variables in the fuction defenition, we are
# creating new variables with scope within the function
# call the function 
# display_sum(8,76)
# display_sum(2026,8)
# display_sum(9.8,6.8)
# display_sum('happy','diwali')

# def display_sum_coustom():
#     print('we will display the sum of 2 numbers you enter')
#     num1=float(input('enter first number:'))
#     num2=float(input('enter the second number:'))
#     sum=num1+num2
#     print('the sum of',num1,'and',num2,'is',sum)
#     display_sum(num1,num2)

# display_sum_coustom()



# def display_name():
#     name=(input('enter your name:'))
#     print('hi',name,'how are you')

# display_name()

#generating multiplication
# num=5
# print('multplication table of number:')
# for i in range(1,11):
#     print(i,'*',num,'=',(i*num))

#function to display multiplication of any number

# def display_multiplication_table():
#     num=int(input('enter a number:'))   
#     for i in range(1,11):
#      print(i,'*',num,'=',(i*num))
        

# display_multiplication_table()
# subject_score=(23,34,25,27,29)

# def main_fuction():
#     score()
#     avarage_of_score()
#     minimum_score()
#     maximam_score()
    

# def score():
#     total_maark=0
#     for i in subject_score:
#        total_maark=total_maark+i
#        i+=1
#     print('sum:',total_maark)
    # avarage_marks=total_maark/len(subject_score)
    # print('avarage marks:',avarage_marks)
    # largest=max(subject_score)
    # print('largest score:',largest)
    # lowest=min(subject_score)
    # print('minimum score:',lowest)


# def avarage_of_score():
    
#     print(len(subject_score))
#     avg=tot


# def minimum_score():
#     print(min(subject_score))

# def maximam_score():
#     print(max(subject_score))  


# # main_fuction() 
# scorelist=(23,32,25,26,25)
# def calculate_sum(scorelist):
#     sum=0
#     for i in range(len(scorelist)):
#         sum=sum+scorelist[i]
#     return sum
    
# total=calculate_sum(scorelist)
# print(total)

#***********************************
#********optional arguments*********
#***********************************
# here exp is an opetional variable
# def calculate_exponent(num,exp=2):
#     print(num**exp)

# calculate_exponent(5)
# calculate_exponent(5,3)    

# def create_wish(name,wish='good day'):
#     print( 'hi', (name),(wish))

# create_wish('abhinav')
# create_wish('abhinav','good morning')
#we can give values of arguments explicitly
#***************************************
print('****************')
def divide(num,den):
    result=num/den
    print('the result is',(result))

# divide(40,5)
# divide(1233,0)  # 0 division error
#**************************************
#exception handling
#we write the criteria so that the code flow is not interrputed
# rewriting te function with exception block
# we write potenlial runtime error making code inside 'try' block
#
def divide_new(num,den):
  try:
       result=num/den
       print('the result is',(result))
  except:
       print('there is problem')


divide_new(45,5)
# divide_new('a','b')
# divide_new(45,0)
# divide_new(45,8)
# divide_new(55,5)
#*****************************
#re writting the function with exception block displaying the error message

def divide_new_(num,den):
   try:
       result=num/den
       print('the result is',(result))
   except Exception as e:
    print('there is problem:',e)


# divide_new_(45,5)
# divide_new_('a','b')
# divide_new_(45,0)
# divide_new_(45,8)
# divide_new_(55,5)

def divide_new2(num,den):
   try:
       result=num/den
       print('the result is',(result))
   except TypeError:
    print('plase sure you entering numbers')
   except ZeroDivisionError:
      print('please make sure to give a no zero value as denominator')
   except Exception as e:
      print(f'there is a problem',{e})
      
print('the end')  

divide_new2(45,5)
divide_new2('a','b')
divide_new2(45,0)
divide_new2(45,8)
divide_new2(55,5)      
      

   
 
    

    




        

