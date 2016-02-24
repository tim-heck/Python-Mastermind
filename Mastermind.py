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
    cows = ["", "", "", ""]
    count1 = 0
    for i in num:
        if str(i) == str(rand_int[count1]):
            cows[count1] = "cow"
        count1 += 1
    return cows


def num_bulls(num, rand_int):
    bulls = ["", "", "", ""]
    count2 = 0
    for i in num:
        if count2 == 0:
            if str(i) == str(rand_int[count2 + 1])\
                    or str(i) == str(rand_int[count2 + 2])\
                    or str(i) == str(rand_int[count2 + 3]):
                bulls[count2] = "bull"
        elif count2 == 1:
            if str(i) == str(rand_int[count2 - 1])\
                    or str(i) == str(rand_int[count2 + 1])\
                    or str(i) == str(rand_int[count2 + 2]):
                bulls[count2] = "bull"
        elif count2 == 2:
            if str(i) == str(rand_int[count2 - 2])\
                    or str(i) == str(rand_int[count2 - 1])\
                    or str(i) == str(rand_int[count2 + 1]):
                bulls[count2] = "bull"
        else:
            if str(i) == str(rand_int[count2 - 3])\
                    or str(i) == str(rand_int[count2 - 2])\
                    or str(i) == str(rand_int[count2 - 1]):
                bulls[count2] = "bull"
        count2 += 1
    return bulls


####################################################


print "Welcome to the Cows and Bulls Game!"
user_num = raw_input("Enter a four digit number: ")

while error_check(user_num) == False:
    user_num = raw_input("Enter a four digit number: ")

print num_cows(user_num, rand_number)
print num_bulls(user_num, rand_number)