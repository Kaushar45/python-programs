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
# print(info.update({"name":"kaushar"})) # updates the dictionary with the specified key-value pair
# print(info.clear()) # removes all the elements from the dictionary
# print(info) # {}