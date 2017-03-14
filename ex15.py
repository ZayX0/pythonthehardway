# System built in module, allowing passing of arguments
from sys import argv

# 'Unpacking' the argumments given on command line/assigning to variables
script, filename = argv

# Assigning the open file command to a variable, basically storing the text
txt = open(filename)


print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
