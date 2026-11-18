file='D:/PGP_ data_science/python/friends.txt'
def read_file():
   try:
     with  open('file','r') as file1:
      read=file1.read()
      print(read)
      file1.close()
   except FileNotFoundError:
      print('file is not found')
         
read_file()

#2
def new_file():
  
  try:
    file=open('file','w') 
    create_file=file.write('abhinav')
    print(f'The file has sucessfylly created',create_file)
  except Exception as e:
      print(f'there is problem {e}')

new_file()   

#3
def add_name():
 try:
  file=open ('file','a')
  add_name=input('name of your friend:')
  file.write('add_name''\n')
  file.close()
  print(f'the name added to {file}')
 except Exception as e:
  print(f'error {e}')

add_name()  

  




  
  
  

  
  

  











 
  