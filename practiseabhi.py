#1
lstname=['abhinav','dhanesh','vishnu','ajith','aakash']
print(lstname)
name=input('enter new student name:')
print('new student name is',name)
lstname.append(name)
print('updated list',lstname)

#2
list1=['rice','sugar','milk']
list2=['bread','eggs','butter']
list1.extend(list2)
print(list1)
print('number of items in list',len(list1))

#3
numbers=[10,20,30,40,10,20,50]
print(numbers)
number1=input('enter a number:')
number1=int(number1)
print(number1)
count=numbers.count(number1)
print('no of times appears:',count)

#4
numbers3=[1,2,3,4,5,6,7,8,9,10]
print(numbers3)
numbers3.reverse()
print(numbers3)

#5
marks1=[78,45,92,56,88,34,67]
print(marks1)
print(marks1.sort())
print(marks1)
marks1.reverse()
print(marks1)

#6
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)
name1=input('enter a fruit name:')
print(name1)
name2=int(input('where should be the fruit add:'))
print(name2)
fruits.insert(name2,name1)
print('uodate fruit list',fruits)

#7
subjects = ["English", "Maths", "Science", "Computer", "History"]
print('orginal list:',subjects)
removed=subjects.pop()
print(subjects)
print('display the removed element:',removed)
print('updated list:',subjects)

#8
colours = ["Red", "Blue", "Green", "Yellow", "Blue"]
print(colours)
color_remove=input('enter a color to remove:')
colours.remove(color_remove)
print('updated list:',colours)

#9
pgm_lang=['pyhon,c,java,html,c++']
print('orginal list:',pgm_lang)
pgm_lang.clear()
print('display updated list:',pgm_lang)
if(pgm_lang==True):
 print('the list is not empty')
else:
 print('list is empty')

#10
students = ["Anu", "Rahul", "Meera", "Arun", "Diya"]
students.append('kiran')
new_student=['sneha','vijay']
students.extend(new_student)
print(students)
students.insert(1,'ravi')
print(students)
print(students.count('Anu'))
students.sort()
print(students)
students.remove('Rahul')
print(students)
students.pop()
print(students)
students.reverse()
print('final attendence list:',students)

