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


def num_cows(num, rand_int):
    cows = 0
    count = 0
    for i in num:
        if count == 4:
            return cows
        elif str(i) == str(rand_int[count]):
            cows += 1
        count += 1
    return cows

def num_bulls(num, rand_int):
    bulls = 0
    for i in num:
        if str(i) == str(rand_int[count + 1]):
            return bulls

####################################################


print "Welcome to the Cows and Bulls Game!"
user_num = raw_input("Enter a four digit number: ")

while error_check(user_num) == False:
    user_num = raw_input("Enter a four digit number: ")

print num_cows(user_num, rand_number)