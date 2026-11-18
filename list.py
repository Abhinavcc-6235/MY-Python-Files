#list is data type used to store collection of value
#since it a is a combimation of other data types( int,float,string,boolean)
#we call it derived data types

#there is no restriction in terms of data types in lists
#a list can contain various type of data =heterogenous

#declaring a list
name=''
name='abhinav'
print(type(name))
#Decalaring a ist
lst_name1  =['name']
print(type(lst_name1))
# #method 2
lst_name2=['vishnu','akash','ajith']
print(type(lst_name2))
#type3
lst_name3=list()
print(type(lst_name3))
#fetching values using index from list
print(lst_name2[0])
print(lst_name2[1])
print(lst_name2[2])
#list containing multiple data types
#personal ifo a list : name,age,graduation,year,unversity,height

amar_info=['amar',34,2026,'cusat',170.5]
print(type(amar_info))    #displaying all information in list
print(amar_info[0])       #display value of index=0
print(type(amar_info[0]))  #display data type of valu at index=0

print(amar_info[1])        #display value of index=1
print(type(amar_info[1]))  ##display data type of valu at index=1

print(amar_info[2])        #display value of index=2
print(type(amar_info[2]))

print(amar_info[3])
print(type(amar_info[3]))

print(amar_info[4])
print(type(amar_info[4]))
#list concantination
list_1=[1,8,3]
list_2=[False,True,False]
print(list_1+list_2)
print(list_2)        #unsorted
print(list_1.sort()) #sorting(ascending)
print(list_1)        # sorted
list_1.sort(reverse=True)  #sorted in ascending
print(list_1)

print(lst_name2.sort())
print(lst_name2)

print(lst_name2.sort(reverse=True))
print(lst_name2)

#extend
lst_name2.extend(list_1)   # extend list
print(lst_name2)
print(lst_name2[3])

#append
list_2.append(list_1)
print(list_2)
print(list_2[3])

list_1.append('A')
print(list_1)

#reverse
# list_1.reverse()
# print(list_1)

#check count of value
print('the number of false appear in the list=',list_2.count(False))
print('the number of true appear in the list=',list_2.count(True))
print("the number of times 'x' appear in the list=",list_2.count('x'))

#value at the last index
print(list_2[-1])
#fetch number of items inthe list
len(list_2)
print('total number of elements in',list_2,len(list_2))

# vale at the last index
print(list_2[-1])
print(list_2[len(list_2)-1])

print('before clear')
print(list_2)

list_2.clear()
print('after clear')
print(list_2)
#**********************

print('before inserting aby value',list_1)
#in order to do #[8,3,1,'A']
#is inserting
list_1.insert(2,100) #inserting  100 at index 2
print('after inserting a value',list_1)
#*************************************

print('before removing 3',list_1)
list_1.remove(3)
print('after removing 3',list_1)
#*********************************
list_1.pop()
print(list_1)
#***************
#**********tuple*********
#**********************
tuple1=()
tuple2=(2026,'nov',2.75,False,[8,True,9.8])
tuple3=tuple()
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(tuple2[2])     #we can catch value using index

print(tuple2.count(False))
print(tuple2.index('nov'))

#once atuple is creeated we can't make any changes to it

del(tuple2)
del(list_2)
# print(tuple2)
# print(list_2)   # get error while running