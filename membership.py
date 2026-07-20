# Membership
# in ======> check for the values in the given data. values present return True 
# not in ===> check for the values in the given data. values not present return True

# students = ["ajmeer", "partha", "bakrudeen", "senthil", "guna", "anbu", "rajan", "ratheesh"]
# print("Partha" not in students)



s = "1234567890"
# print("A" in s)
# print("A" not in s)


#Membership in DICT
student = {
    "name": ["Partha" ,"bakrudeen" , "shek", "abinaya"],
    "age": 20, 
    "place": ["Karur","salem"],
    "email": "abcd1234@gmail.com"
}
print("name" in student)   #searching KEY
print("Partha" in student)
print("Partha" in student["name"])  # searching VALUES
print("madurai" not in student["place"])




