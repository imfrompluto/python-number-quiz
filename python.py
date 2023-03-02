# print(23)
# print("hello")
# name = "max"
# food = "chips"
# print(name)
# print(name + " likes pizza")
# name = "sam"
# print(name + " likes " + food)
# myname = input("what is your name?")
# print("good evening " + myname)
import random

print("do you want to play this game on hard mode or easy mode")
mode = input("hard or easy mode? ")
if mode == "easy":
    print("the computer thought of a number between 1 and 20. try to guess it")
    secretnumber = random.randint(1,20)
    # secretnumber = 5
if mode == "hard":
    print("the computer thought of a number between 1 and 40. try to guess it")
    secretnumber = random.randint(1,40)
    # secretnumber = 8
if mode == "easy" or mode == "hard":
    hearts = 5
    while hearts > 0:
        print("you have " + str(hearts) + " lives")
        usernumber = input("guess the number: ")
        if secretnumber == int(usernumber):
            print("you win!")
        if usernumber == "777":
            print("you win!")
            break
        else:
            hearts = hearts - 1
            if secretnumber > int(usernumber):
                print("incorrect answer, the number is higher")
            else:
                print("incorrect answer, the number is smaller")
                # needed so that when you win it doesnt say you lose
    if hearts == 0:
        print("you lose! the answer was " + str(secretnumber))






# if a person write some number like 777 they instantly win
