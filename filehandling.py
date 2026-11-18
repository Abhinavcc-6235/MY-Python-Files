#*******************************
#********FILE HANDLING**********
filepath='D:/PGP_ data_science/python/test.txt'
ralative_filepath= ('test.txt')
file=open(filepath,'r') #assign file in reading mode

cotent=file.read()  #ontents of the file is assigned to content
print(cotent)


# trying using relative file path
def read_file_rel_filepath():
    file_1=open(ralative_filepath,'r')
    content1=file_1.read()
    print(content1)
    file_1.close()

read_file_rel_filepath()

def read_line_by_lines():
    file=open(filepath,'r')
    content2=file.readline()
    print(content2)
    file.close

read_line_by_lines()    

def read_lines():
    file=open(filepath,'r')
    content3=file.readlines()
    print(content3)
    file.close

read_lines()

#**********************************
#*********write a field*************
#**********************************
#opens a file in writting mode
# if the file didn't exist earlier,it will be created
# and opens in writting mode
write_path='students.txt'
def write_a_file():
    file=open(write_path,'w')
    file.close()

# write_a_file()

def write_a_file1():
    file=open(write_path,'w')
    file.write('gowtham\n')
    file.write('vishnu\n')
    file.write('aakash\n')
    file.close()


# write_a_file1()


def course(course):
    file=open(write_path,'w')
    file.write(course)
    file.close
    

# course('data science')

# append data into the file
def append_file():
    file=open(write_path,'a')
    file.write('keerthi')

# append_file()

#converting into generic function into a file 

def append1(filepath,i_name):
    file=open('\n')
    file=open(filepath,'a')
    file.write(i_name)
    # file.write('gowtham\n')
    # file.write('vishnu\n')
    # file.write('aakash\n')
    file.close()

append1('test file text','bsnl')    
# this methode is more prefred
def append2(filepath,i_name):
    file=open('\n')
    with open(filepath,'a') as file:
    file.write(i_name)
append2('test file text','airtel')     