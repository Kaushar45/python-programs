str1="This is a string./nwe are creating it in python" 
print(str1)
print(len(str1)) #lenght of string
# /n for next line
# /t for tab

# concatenation
str1="hello"
str2="world"
print(str1+" "+str2)

# indexing
str="kaushar"
i=str[0]
print(i)

#accessing part of index
#str[starting inde : ending index]
print(str[2:])
# negative index
print(str[-4:-1]) #not including -1

# string functions
str="i am studying python"
print(str.endswith("hon"))
print(str.capitalize())
print(str.replace("python","javaScript"))
print(str.find("python")) # return first index
print(str.count("i"))

#Write a program input user's first name & print its lenght
chr=input("your name :")
print(len(chr))

#Write a program to find occurrence of '$' in a string
count="hi i'm $ symbol" 
print(count.count("$"))

#Conditional Statement
age=1
if(age>=18):
    print("can vote & apply for licence") #indentation
    print("can drive")
else:print("cannot vote")
print("cannot drive")

light="yellow"
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("Go")
else:print("light is broken")

#grade students based on marks
marks=int(input("your marks :"))
if(marks>=90):print("grade-'A'")
elif(90>marks>=80):print("grade-'B'")
elif(80>marks>=60):print("grade-'C'")
elif(60>marks>=35):print("grade-'D'")
else:print("grade-'E'")

# both same 
marks=int(input("your marks :"))
if(marks>=90):grade='A'
elif(90>marks>=80):grade='B'
elif(80>marks>=60):grade='C'
elif(60>marks>=35):grade='D'
else:grade='E'
print(grade)

#Write a program to check if a number entered by the user is odd or even.
num=int(input("Enter Number:"))
if(num%2==0):
    print("Even")
else:print("odd")


#Write a program to find the grestest of  numbers entered by the user
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
c=int(input("Enter Number:"))

if(a>=b and a>=c):
    print("first number is largest number",a)

elif(b>=a and b>=c):
    print("second number is largest number",b)
else:print("third number is largest number",c)

#Write a program to find the grestest of 4 numbers entered by the user
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
c=int(input("Enter Number:"))
d=int(input("Enter Number:"))


if(a>=b and a>=c and a>=d):
    print("first number is largest number:",a)

elif(b>=a and b>=c and b>=d):
    print("second number is largest number:",b)

elif(c>=a and c>=b and c>=d):
    print("third number is largest number:",c)

else:print("fourth number is largest number:",c)


#Write a program to check if a number is a multiple of 7 or not
num=int(input("Enter Number:"))

if(num%7==0):
    print("Multiple of 7")
     
else:print(" Not Multiple of 7")