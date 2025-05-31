# Dictionary

# Dictionary is a collection of key-value pairs.
# Dictionaries are used to store data values in 'key:value' pairs. 
# A dictionary is a mutable(changeable), unordered &  dont allow duplicates keys.

info={
    "name":"kaushar",
    "subjects":["Python","Javascript","C++"],
    "marks":95.5,
    "is_student":True,
    34.7:45
}
print(type(info)) # <class 'dict'>
info["name"] = "Kaushar"   #override the value of key
info["age"] = 19 # add new key-value pair
print(info["name"]) # kaushar
print(info["subjects"]) # ['Python', 'Javascript', 'C++']
print(info["marks"]) # 95.5
print(info)

# Nested Dictionary
info ={
    "name":"kaushar",
    "score": {
        "python":95,
        "javascript":90,
        "c++":85
    }
}
print(list(info.keys()))  
print(info["score"]["python"]) # 95

# Dictionary Methods
print(info.keys()) # returns a list of all the keys in the dictionary
print(info.values()) # returns a list of all the values in the dictionary
print(info.items()) # returns a list of all the key-value pairs in the dictionary
print(info.get("name")) # returns the value of the specified key
print(info["name"]) # returns the value of the specified key
print(info.pop("name")) # removes the specified key and returns the value
print(info.popitem()) # removes the last inserted key-value pair
info.update({"name":"kaushar", "class":"12"}) # updates the dictionary with the specified key-value pair
# # print(info.clear()) # removes all the elements from the dictionary
print(info) # {}
    

# Set
# A set is a collection which is unordered, unchangeable, and unindexed.

collection = {1, 2, 3, 4, 5,"hello", "world","world", 1, 2, 3} # duplicate values are not allowed
print(collection) # {1, 2, 3, 4, 5, 'hello', 'world'}
print(type(collection)) # <class 'set'>
print(len(collection)) # 7
null_set = set() # empty set
print(null_set) # set()
print(type(null_set)) # <class 'set'>

# set methods 
collection.add(6) # adds an element to the set
print(collection) # {1, 2, 3, 4, 5, 'hello', 'world', 6}
collection.remove(6) # removes the specified element from the set
print(collection) # {1, 2, 3, 4, 5, 'hello', 'world'}
collection.discard(5) # removes the specified element from the set, if it exists
print(collection) # {1, 2, 3, 4, 'hello', 'world'}
collection.pop() # removes a random element from the set
print(collection) # {2, 3, 4, 'hello', 'world'} (the output may vary)
collection.clear() # removes all the elements from the set
print(collection) # set()

collection.union() # returns a set that contains all the elements from both sets
collection.intersection() # returns a set that contains only the elements that are present in both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}

# Question 1
# store following word meaning in a python dictionary.
word_meaning = {
    "abate": "to lessen in intensity or degree",
    "benevolent": "well-meaning and kindly",
    "candid": "truthful and straightforward",
    "diligent": "having or showing care in one's work or duties",
    "empathy": "the ability to understand and share the feelings of another"
} 
print(word_meaning)

# Question 2
# create a set of unique subject from the following list
subjects = ["python", "javascript", "c++", "python", "java", "javascript","javascript","C", "c++", "python"]
unique_subjects = set(subjects)
print(unique_subjects)
print(len(unique_subjects))  # prints the number of unique subjects

# Question 3

# Write a program to enter marks of 3 subjects from the user and store them in a 
# dictionary. Start with an empty dictionary and add one by one. Use the subject name as key and marks as value.
marks_dict = {}
x = int(input("Enter marks for Mathematics: "))
# marks_dict["Mathematics"] = x
marks_dict.update({"Mathematics": x})

x = int(input("Enter marks for Science: "))
# marks_dict["Science"] = x
marks_dict.update({"Science": x})

x = int(input("Enter marks for English: "))
# marks_dict["English"] = x
marks_dict.update({"English": x})

print(marks_dict)

# Question 4
# Figure out a way to store 9 & 9.0 as separate values in the set.
# (take help of build-in data types)
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)  # {('float', 9.0), ('int', 9)}