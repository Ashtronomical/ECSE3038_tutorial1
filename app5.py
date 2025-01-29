squares = [] 
even_numbers = []
upper_case_names = []

# a. Starting with an empty list, append the squares for the numbers from 1 to 5 using a for loop.
# b. Starting with an empty list, append the even numbers from 2 to 10 (inclusive) using a for loop.
# c. Using a for loop, create a list of names in uppercase from the list of people in Exercise 3.

for number in range(1,6):
    squares.append(number * number)



people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]
for person in people:
    upper_case_names.append(person["name"].upper())

print(squares)
print(upper_case_names)


