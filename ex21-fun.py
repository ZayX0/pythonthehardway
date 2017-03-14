def get_username():
    name = raw_input("What would you like your username to be? ")
    return name

user_name = get_username()

print "Your username is %s, excellent!" % user_name
