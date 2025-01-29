#Given the following dictionary representing a person:
person= {
    "name": "Alice",
    "age": 28,
    "city": "Wonderland"
}
#a. Print the person's name.
#b. Add a new key-value pair to represent the person's occupation (e.g., engineer)
#c. Update the person's age to 29
#d. Remove the city from the key dictionary 
#e. Print the keys of the modified dictionary

print("name:"+person["name"]) #a
person.update({"occupation": "engineer"}) #b
person.update({"age": 29}) #c
del person["city"] #d
print(person.keys()) #e




