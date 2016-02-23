#################################
# Mastermind python mini project
# Tim Heck
# 02/23/16
#################################

from random import randint

# Creates random four digit number as a string
rand_number = ""
count = 0
while count < 4:
    rand_number += str(randint(0, 9))
    count += 1

print rand_number

####################################################


def error_check(n):
    if len(n) < 4 or len(n) > 4:
        print "The number entered is the a four digit number"
        return False
    return True


def check_guess(num, rand_int):
    cows_bulls = ["", "", "", ""]
    count1 = 0
    for i in num:
        if str(i) == str(rand_int[count1]):
            cows_bulls[count1] = "cow"
        count1 += 1

    count2 = 0
    if cows_bulls[count2] == "cow":
        count2 += 1
    if cows_bulls[count2] == "bull":
        count2 += 1
    for i in num:
        if str(i) == str(rand_int[count2 + 1]):
            if count + 1 > 4:
                return cows_bulls
            cows_bulls[count + 1] = "bull"
            if count + 2 > 4:
                return cows_bulls
        if str(i) == str(rand_int[count2 + 2]):
            if count + 2 > 4:
                return cows_bulls
            cows_bulls[count + 2] = "bull"
            if count + 3 > 4:
                return cows_bulls
        if str(i) == str(rand_int[count2 + 3]):
            if count + 3 > 4:
                return cows_bulls
            cows_bulls[count + 3] = "bull"
        count2 += 1
    return cows_bulls


####################################################


print "Welcome to the Cows and Bulls Game!"
user_num = raw_input("Enter a four digit number: ")

while error_check(user_num) == False:
    user_num = raw_input("Enter a four digit number: ")

print check_guess(user_num, rand_number)