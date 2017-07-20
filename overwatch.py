# -*- coding: utf-8 -*-
choice_one = ""

def opening():
    print "Welcome to the Overwatch hero assigner! We’ll ask you some scenario based questions and we’ll tell you what Overwatch hero fits you best!"
    raw_input("If you'd like to continue, press ENTER, if not press CTRL+C")
    q1(0)

def q1(user_score):


    print "Welcome to the game! Below is your first question\n"
    choice_one = raw_input("A 10v10 brawl is about to happen, your team is developing a strategy, what role do you want?\n\na) Don’t care as long as I get to throw the first punch\nb) I’ll defer my role to what the group decides for me\nc) Why are we fighting?\nd) I want to be one who jumps in and turns a 1v1 fight in my persons favor\ne) Kamikaze\n> ")
    if choice_one == "g":
        user_score += 25
    elif choice_one == "b":
        user_score += 5
    elif choice_one == "c":
        user_score += 0
    elif choice_one == "d":
        user_score += 10
    elif choice_one == "e":
        user_score += 15

    return user_score

question1 = q1()

def final_tally(q1):
    final_score =


def question_2():
    choice_two = raw_input("Which number is most appealing to you?\na) 10\nb) 20\nc) 30\nd) 40\n> ")


opening()
