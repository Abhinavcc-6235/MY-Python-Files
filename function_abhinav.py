
#1 
def calculator():
    num1=float(input('enter the first number:'))
    num2=float(input('enter the second number:'))
    operator=input('enter the opertor')
    if operator=='+':
         operators=(num1+num2)
         return operators
    
    elif operator=='-':
        operators=(num1-num2)
        return operators
    elif operator=='*':
        operators=(num1*num2)
        return operators
    elif operator=='/':
        operators=(num1/num2)
        return operators
 
calculator1=calculator()
print('answer',calculator1)

#3
def simple_intrest():
    principle=int(input('enter the principle:'))
    rate=float(input('enter the rate:'))
    time=float(input('enter the time:'))
    intrest=principle*rate*time/100
    return intrest


simple_intrest1=simple_intrest()
print(simple_intrest1)
  
#4
def last_character(apple):
    return apple[-1]
print(last_character('apple'))

# #5
def  calculate_bill(units):
    if units<=100:
        bill=units*5
    elif units<=200:
        bill=units*7+100*5
    else:
        bill=100*5 + 100*7 + units-200*10
    return bill

total_amt=calculate_bill(100)  
print('bill',total_amt) 

#6
def  count_even(even_numbers):
    count=0
    for i in (even_numbers):
        if i%2==0:
            count+=1
    return count

list=(34,76,88,97)
print('even number:',count_even(list))



