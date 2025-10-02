# Loops
# Loops are used to repeat instruction.
# while Loops 
count =1 # Iterator 
while  count<=5:
    print("Hello World") # Iteration
    count+=1

# 1. print number from 1 to 100

count = 1
while count <=100:
    print(count)
    count +=1

 # 2. print number from 100 to 1
count =100
while count>=1 :
    print(count)
    count-=1 

# 3. print the multiplication table of a number n
n = int(input("Enter Number : " ))
tab = 1
while tab <=10:
    print(n*tab)
    tab +=1

# 4. print the element of the following list using a loop 
list=[1,4,9,16,25,36,49,64,81,100]
i = 0
while i <len(list):
    print(list[i])
    i +=1

# 5. search for a number x in this tuple using loop 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 120
i = 0
found = False

while i < len(nums):
    if nums[i] == x:
        print(i)
        found = True
        break
    i += 1

if not found:
    print("Not Found")


# Break & Continue
# Break : used to terminate the loop when encountered
# Continue : terminate execution in the current iteration & continue execution
#  of the loop with the next iteration.
 
#  Loops in Python
#  Loops are used used for sequential traversal. For traversing list, string, tuples etc.
#  for Loops
#  for el in list: 
 
list=[1,2,3]
for el in list : 
    print(el)

# for Loop with else
# for el in list: 
# #some work
#  else: 
# #work when loop ends 

for el in list : 
    print(el)
else:
    print("End")

tup = (1,2,3,4,5,78,987,9,0)
for num in tup:
    print(num)

text = 'helloWorld'

for char in text:
    if(char =="W"):
        print("W found")
        break
    print(char)
else:
    print("End")

# practice
# 1. print the element of the following list in using a loop

nums = [ 1,4,9,16,25,49,64,81,100]

for num in nums:
  print(num)  

# 2. Search for a number x in this tuple using loop 

numbers = (1, 4, 9, 16, 25, 49, 64, 81, 100, 16)
x = 16
idx = 0

for num in numbers:
    if num == x:
        print("Found at index", idx)
    idx += 1

# Range()
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified numbers.

# range(start?,stop,step?)    

print(range(5)) # range(0,5)

seq = range(5)
print(seq[0]) #0
print(seq[1]) #1
print(seq[2]) #2
print(seq[3]) #3
print(seq[4]) #4

for i in seq:
    print(i) 

for i in range(11): #range(stop)
    print(i)    

for i in range(3,11,3): #range(start?,stop,step?)
    print(i)

# practice
# print numbers from 1 to 100
for num in range(1,101,1):
    print(num)

# print numbers from 100 to 1
for num in range(100,0,-1):
    print(num)

# print multipliction table of a number n
n= int(input("Enter Number: "))
for table in range(n,n*11,n):
    print(table)

# pass statement
# pass is a null statement that does nothing. It is used as a placeholder for future code
for el in range(11):
    pass
if el>5:
    pass
print("some work")

# practice
# 1. write a program find the sum of first n numbers (using while)

n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)  # Output: 15

# 2. write a program find the factorial of first n numbers. (using for) 

num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
    print(f"Factorial of {i} is {fact}")
