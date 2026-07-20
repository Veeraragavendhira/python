#A dictionary is a data type in Python used to store data in key-value pairs.
#Each key is unique and is used to access its corresponding value.
student = {
    "name": ["Partha" ,"bakrudeen" , "shek", "abinaya"],
    "age": 20, 
    "place": "Karur",
    "email": "abcd1234@gmail.com"
}
print(student)
print(type(student))
print(student["name"],student["age"], student["place"]) 
print(student["name"][2])
