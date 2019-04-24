list_of_vehicles = ["Truck", "Car", "Scooter"]
# Iterating over an iterable
print("------------Iterating------------")
for vehicle in list_of_vehicles:
    print("The vehicle is {0}".format(vehicle))

print("------------Enumerate------------")
for index, vehicle in enumerate(list_of_vehicles):
    print("The vehicle in index {0} is {1}".format(index, vehicle))

# Idiomatic way to access it
print("------------List comprehension------------")
[print(vehicle) for vehicle in list_of_vehicles]

print("------------List comprehension with conditional------------")
[print(vehicle) for vehicle in list_of_vehicles if vehicle != 'Truck']

print("------------A Matrix------------")
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row_index, row in enumerate(matrix):
    for column_index, value in enumerate(row):
        print("({0},{1}): {2}".format(row_index, column_index, value))

print("------------Nested list comprehension------------")
words = ['cat', 'dog', 'rabbit']
[print(letter) for word in words for letter in word]
