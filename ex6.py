# Set string value to number of people
x = "There are %d types of people." % 10

# Set binary string to variable
binary = "binary"

# Set 'don't' to variable
do_not = "don't"

# Call variables to place in string
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x to console
print x

# Print y to console
print y

# Print x in %r format (exactly reproduce)
print "I said: %r." % x

# Print y in string format
print "I also said: '%s'." % y

# Set False variable
hilarious = False

# Set string to variable with internal variable to change output
joke_evaluation = "Isn't that joke so funny?! %r"

# Show joke_evaluation var to console with hilarious as internal variable
print joke_evaluation % hilarious

# Set string to w variable
w = "This is the left side of.."

# Set string to e vairable
e = "a string with a right side."

# Combine w and e strings, print to console
print w + e
