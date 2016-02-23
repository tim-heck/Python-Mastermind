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

print "Welcome to the Cows and Bulls Game!"
user_num = raw_input("Enter a four digit number: ")

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

print num_cows(user_num, rand_number)
