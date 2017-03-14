# Assign number of cars
cars = 100
# Assign amount of space in each car
space_in_a_car = 4
# Assign number of drivers
drivers = 30
# Assign number of passengers
passengers = 90
# Calculate the total number of cars not being driven/have no drivers
cars_not_driven = cars - drivers
# Assign how many cars are being driven/have drivers
cars_driven = drivers
# Calculate total capacity of people in carpool
carpool_capacity = cars_driven * space_in_a_car
# Calculate average number of passengers per car
average_passengers_per_car = passengers / cars_driven

# Print out values into strings as appropriate

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
