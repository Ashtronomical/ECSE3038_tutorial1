# a. Create a list of dictionaries, where each dictionary represents a person.
people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]

# b. Print the name of the second person in the list.
# c. Update the age of the third person to 30.
# d. Add a new person to the list.
# e. Print the list after the modifications.

print("Second person name:", people[1]["name"]) #b
people[2]["age"]= 30 #c
newPerson = {"name": "Ash","age":24,"city": "Kingston"} #d
people.append(newPerson) #d
for person in people:
    print(person)
