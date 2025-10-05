# File I/O
#  Python can be used to perform operations on a file. (read & write data)

# Open, read & close File
file = open("demo.txt","r")
data = file.read() #reads entire file
print(data)
print(type(data))
file.close() 


file = open("demo.txt","r")
line1 = file.readline() #reads one line at a time
print(line1)

line2 = file.readline() 
print(line2)

file.close()

file = open("demo.txt",'w')
file.write("This is a new line") #overwrites the entire file

file = open('demo.txt','a')
file.write("\nThis is a new line") #adds to the file


file = open('demo.txt','r+')
file.write("abc")
file.close()

# with Syntax
with open('demo.txt','r') as f:
 data = f.read( ) 
 print(data)

with open('demo.txt','w') as f:
 data = f.write("hello, new data" ) 
 print(data)

# Deleting a File
#  using the os module
#  Module (like a code library) is a file written by another programmer that generally has a functions we can use.

import os
os.remove('demoEx.txt')

#  Practice
#  1.Create a new file “practice.txt” using python. Add data in it: 
file = open('practice.txt','w')
data = file.write("Hi everyone")
print(data)
print(type(data))

with open('practice.txt','w') as f:
    f.write('hello,\nwe are learning File I/O\nusing JavaScript.\nI like programming in JavaScript')
          
# 2.replace all occurrences of “JavaScript” with “Python” in above file.
with open('practice.txt','r') as f:
    data = f.read() 
    new_data= data.replace('JavaScript','Python')   
    print(new_data)  

with open('practice.txt','w') as f:
    f.write(new_data)

# 3.Search if the word “learning” exists in the file or not. 
word ='learning'
with open('practice.txt','r') as f:
    data= f.read()    
    if (data.find(word) != -1):
        print("found")
    else:
        print("not found")

# 4. write a function to find in which line of the file does the word “learning”occur first. Print -1 if word not found. 
def check_for_line():
    word = 'learning'
    line_no = 1
    with open('practice.txt', 'r') as f:
        for line in f:
            if word in line:
                print(line_no)
                return  # Exit after first match
            line_no += 1
    print(-1)  # If word not found
check_for_line()

# 5.From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(',')
    for val in nums:
        val = val.strip() 
        try:
            number = int(val)
            if number % 2 == 0:
                count += 1
        except ValueError:
            continue

print("Count of even numbers:", count)
