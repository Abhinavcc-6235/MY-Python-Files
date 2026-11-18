
python=55
mathematics=30
science=50

def main_function():
 total=calculate_mark()
 largest=avarege_mark()
 largest=largest_mark()
 lowest=lowest_mark()
 certificate()
  

def calculate_mark():
  total =(python+mathematics+science)
  print('total marks:',total)
  return total


def avarege_mark():
  avarege_mark=calculate_mark()/3
  print('avarege marks:',avarege_mark)


def largest_mark():
 largest=max(python,mathematics,science)
 print('largest score:',largest)

def lowest_mark(): 
 lowest=min(python,mathematics,science)
 print('minimum score:',lowest)
 
def certificate():
  print('python:',python>40)
  print('mathematics:',mathematics>40)
  print('science:',science>40)

main_function()


#2

 


