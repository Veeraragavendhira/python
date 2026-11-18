#A dictionary is a data type in Python used to store data in key-value pairs.
#Each key is unique and is used to access its corresponding value.
student = {
    "name": ["Partha" ,"bakrudeen" , "shek", "abinaya"], 
    "age":  (20, 12, 10 ),
    "place": ["Karur","salem", "chennai" ],
    "email": ["abcd1234@gmail.com"]
}

# print(student)
# print(type(student))
# print(student["name"],student["age"], student["place"]) 
print(student["place"][-1])
print(student["email"][-1])
print(student["name"][0])
print(student["age"][-1])
print(student["name"][0], student["age"][0], student["place"][0], student["email"][0])