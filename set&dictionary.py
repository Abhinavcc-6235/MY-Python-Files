#******************************
#*********SET******************
#******************************

#declaring a set
#methode 1
set={}     #not a set this is dictionary
#methode2
set2={12,55,88,True,'bsnl',2026,2026.0,'2026'}    #set
#methode3
set3= set

print(type(set))
print(type(set2))
print(type(set3))
print(set2)
#***************************************
#values were displayed but not in order
#set support all data types ie; hetrogenous
#duplicates are denied.
#***************************************
roll={1,2,3,4,5,6}
roll_odd={1,3,5}
roll_even={2,4,6}
random={1,5,9,4}
random.add(2026)
print(random)
#********************************
print(random.difference(roll_odd))
print(roll_odd.difference(random))
#*********************************
print(roll.issuperset(roll_odd)) #true
print(roll.issubset(roll_odd))    #false
print(roll.issuperset(random))    #false

#intersection (commo )
print(random.intersection(roll_odd)) #common in both sets
print(random.intersection(roll_even))
#union(combining)
print(random.union(roll_even))
#remove
random.remove(1)
print(random)

#properties of set
#*******************
#proprtis of data  type set
#supportt hetergenous data type
#*****************************
#*********Dictionary**********
#*****************************
dict1={}  
#methode2
dict2={'key1':'value','key2':'value2','b':2026} 
dict3=dict()
print(type(dict1))
print(type(dict2))
print(type(dict3))
print(dict2)     #dictionary has a key value pair
#dictionry key and values can be of any data type
sampl_dict={1:'one',0:'zero',1:'true',1:'ICT'}
print(sampl_dict)
print(dict2['key2'])

stuent_dict={'name':'abhinav',
             'age':25,
             'university':'kannur',
             'district':'wynd'}
print('whole dictinary',stuent_dict)
#keys
print('keys are')
print(stuent_dict.keys())
#values
print('values are')
print(stuent_dict.values())
#items
print('items are')
print(stuent_dict.items())
#modifying value of key
stuent_dict['university']
print(stuent_dict)

personadict={'name':'abhinav','age':'25','district':'wayanad',
             'course':'data science','institution':'ict'}
print(personadict)