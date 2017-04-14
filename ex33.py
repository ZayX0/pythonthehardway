"""def my_loop(i, pass_number, jumper):
    while i <= pass_number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += jumper
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i """

def my_for_loop(i, run_amt):
    for i in range(0,run_amt):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers

print "What number should I stop at?"
run_time = int(raw_input("> "))

print "How much should I count up by?"
count_up_by = int(raw_input("> "))

i = 0
numbers = []

my_for_loop(i, run_time)
print "The numbers: "

for num in numbers:
    print num,
