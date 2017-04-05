i = 0
numbers = []

def my_loop(i, pass_number):
    while i < pass_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print "How many teams do you have?"
teams = int(raw_input("> "))

my_loop(i, teams)
print "The numbers: "

for num in numbers:
    print num
