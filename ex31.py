print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "Welcome to the Matrix, do you take the red pill, or blue?"
    print "1) Red Pill"
    print "2) Blue Pill"

    pill = raw_input("> ")

    if pill == "1":
        print "That pill was actually poison...you're dead"
    elif pill == "2":
        print "You have been granted super powers for eternity, congrats!"
    else:
        print "You wake up in your bed and realize it was all a dream."

elif door =="2":
    print "You hear a voice asking you to close your eyes and take 3 steps forward..."
    print "1) Follow the voices instructions"
    print "2) Ignore the instructions entirely"

    voice = raw_input("> ")

    if voice == "1":
        print "It was an evil spirit and you walked into its mouth and it ate you, tough break"
    elif voice == "2":
        print "You do your own thing and close the door back as you hear the voice grumble, congrats you survived"
    else:
        print "You stand frozen and are now stuck in this dark room forever...should have made a valid choice"

else:
    print "You have broken the space time continuim and see a Game Over screen"
