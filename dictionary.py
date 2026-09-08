student = {
    "name": "Harry",
    "age": 25,
    "city": "Delhi"
}
print(student)

print(student.get("city")) #Values are accessed using keys
student.pop("age")
print(student)
student['sex'] = "male" #adding new key value pair
print(student)
student.popitem() # poptime method last key value ko remove krta hai
print (student)
del student['city'] # del method use krke bhi bhi hum hta skte hain key values ko
print(student)
