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
