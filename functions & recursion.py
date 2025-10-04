# functions
# Block of statements that performs a specific task.

def sum(a, b):
    s = a + b
    print(s)
    return s
print(sum(6,3))
sum(4,4)

def calc_avg(a,b,c):
    avg = (a+b+c)/3
    print(avg)

calc_avg(2,4,2)    
   
# Default Parameters  
# Assigning a default value to parameter, which is used when no argument is passed.

def multipliction(a,b=2):
    m= a*b
    print(m)
multipliction(3)      

# Practice
# 1. print the lenght of a list. (list is the parameter) 
cities=['delhi','mumbai','noida','locknow','pune']
def print_len(list):
    print(len(list))
print_len(cities)
     
# 2. print the elements of a list in a single line. ( list is the parameter)
cities=['delhi','mumbai','noida','locknow','pune']

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)        

# 3. find the factorial of n. (n is the parameter)
def fact(num):
    fact = 1
    for i in range(1, num + 1):
     fact *= i
     print(f"Factorial of {i} is {fact}")

fact(3)     
 
# 4. WAF to convert USD to INR. 
def converter(usd_val):
   inr_val =usd_val*83
   print(usd_val,"USD =", inr_val,"INR" )

converter(100)  

# Recursion- when a function calls itself repeatedly

# Recursive function
def show(n):
    if ( n == 0): # base case
        return
    print(n)
    show(n-1)
show(5)

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
    
print(fact(5))
print(fact(0))  

#  Practice
# 1. Write a recursive function to calculate the sum of first n natural numbers. 
  
def sum(n):
    if n == 0:
        return 0
    return sum(n - 1) + n

print(sum(5))

# 2. Write a recursive function to print all elements in a list
#    Hint : use list & index as parameters.

def print_list(list,idx):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

lst = [3,4,556,8,97,79,65]
 
print_list(lst,3)