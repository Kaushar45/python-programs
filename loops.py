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

