#1
fruits={'Apple''Banana','orange', 'Mango', 'Grapes'}
print(fruits)
num=len(fruits)
print('number of elements present in set:',num)

#2
numbers = [10, 20, 10, 30, 20, 40, 50, 30]
numbers=set(numbers)
print('after removing duplicate values:',numbers)

#3
colors={"red", "blue", "green"}
colors.add("yellow")
colors.add( "black")
colors.add( "blue")
print('final set:',colors)

#4
student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"}
print('subject that both student study:',student1.intersection(student2))

#5
student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"}
print('all subjects:',student1.union(student2))
print(student1)
print(student2)

#6
student={'name':'rahul','age':20,'course':'python','city':'kochi'}
print('complete dictionary:',student)
print('students name:',student['name'])
print('student age:',student["age"])
print('student course:',student["course"])

#7
employee = { "name": "Anu", "age": 25, "salary": 25000}
print(employee)
employee.update({"department":"it"})
print(employee)
employee.update({"salary":30000})
print(employee)
employee.update({"age":26})
print(employee)
print('updated dictionary:',employee)
#8
marks = { "Maths": 80, "Science": 75, "English": 90,
"Computer": 85}
print(marks.keys())
print(marks.values())
total_mark=marks["Maths"]+marks["Science"]+marks["English"]
print(total_mark)
avg=(total_mark)/len(marks)
print(avg)

#9

student = {"name": "Arun", "age": 21, "course": "Python",
"marks": 85}
print(student)
if (student["marks"]>50):
    print('pass')
else:
    print('fail')
student.update({"grade":"A"}) 
print(student) 
while(student["name"],student["age"],student["course"],student)


#10
morning_batch = {"Anu", "Rahul", "Arun", "Meera"}
evening_batch = {"Rahul", "Meera", "John", "Priya"}
print(morning_batch.intersection(evening_batch))
print(morning_batch.union(evening_batch))
print(morning_batch)
print(evening_batch)