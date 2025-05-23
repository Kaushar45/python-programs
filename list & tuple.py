# List
# A built-in data type that lets us create mutable sequences of values.
marks=[85, 90, 78, 92, 88]
print(marks)
print(type(marks)) # list
print(marks[0]) # 85
print(marks[1]) # 90
print(len(marks)) # 5
print(marks[:3]) # [85, 90, 78]

# string are immutable
# list are mutable
# mutable means we can change the value of list
# immutable means we cannot change the value of string

# str="hello"
# print(str[0]) # h
# str[0]='H' # error

student=["kaushar", 20, 85.5, True]
print(student)
student[0]='hello'
print(student)


# list slicing

# list_name[starting index : ending index]
marks = [85, 90, 78, 92, 88]
print(marks[1:3]) # [90, 78]
print(marks[2:]) # [78, 92, 88]
print(marks[:3]) # [85, 90, 78]
print(marks[-3:-1]) # [78, 92]
print(marks[-3:]) # [78, 92, 88]

# list methods
list = [ 4,2, 3 ]
list.append(1) # adds one element at the end of the list 
print(list) # [4, 2, 3, 1]

list.sort() # sorts the list in ascending order 
print(list) # [1, 2, 3, 4]

list.reverse() # reverses the list 
print(list) # [4, 3, 2, 1]

list.sort(reverse=True) # sorts the list in descending order 
print(list) # [4, 3, 2, 1]

#list.insert(idx, el)  inserts the element at the given index
list.insert(2, 3) # inserts the element at the beginning of the list
print(list) # [4, 3, 3, 2, 1]

list.remove(3) # removes the first occurrence of the element from the list
print(list) # [4, 3, 2, 1]

list.pop() # removes the last element from the list
print(list) # [4, 3, 2]
list.pop(1) # removes the element at the given index
print(list) # [4, 2]

# Tuple-----------------------------------
# A build in data type that lets us create immutable sequences of values.
# Tuples are defined using parentheses () instead of square brackets [].

tup = (1)
print(type(tup)) # <class 'int'>
# To create a tuple with a single element, we need to add a comma after the element.
tup = (1,)
print(type(tup)) # <class 'tuple'>
# A tuple can contain elements of different data types.

tuple = (2, 1, 4, 3,1.5, "hello", True)
print(type(tuple)) # <class 'tuple'>
print(tuple[1:3]) # (1, 4)
print(tuple[2:]) # (4, 3, 1.5, 'hello', True)

# tuple.index(el) # returns the index of the first occurrence of the element in the tuple
print(tuple.index(2)) # 0
print(tuple.count(2)) # 1

# tuple.count(el) # returns the number of occurrences of the element in the tuple
# tuple.index(el) # returns the index of the first occurrence of the element in the tuple

print(tuple.count(1)) # 2

# Practice Questions

# 1. Write a Program to enter name of their 3 favorite movies and store them in a list. Then print the list.
movieList=[]
movieList.append(input("First movie Name: "))
movieList.append(input("Second movie Name: "))
movieList.append(input("Third movie Name: "))
print(movieList)

# 2. write a program to check is a list containt a polindrome of elements.(hint: use copy() and reverse() method).

polindrome = [1, 2, 3, 2, 1]
polindrome=[1,"abc","abc",1]
polindromeCopy = polindrome.copy()
polindromeCopy.reverse()
if polindrome == polindromeCopy:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

# 3. write a program to count the number od students with the "A" grade in the following tuple
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))
print(grade.count("B"))
print(grade.count("C"))
print(grade.count("D"))

grade_sort=["C","D","A","A","B","B","A"]
grade_sort.sort()
print(grade_sort)