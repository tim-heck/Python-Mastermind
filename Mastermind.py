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


# Method to check if the user entered number is
# a four digit number
def error_check(n):
    if len(n) < 4 or len(n) > 4:
        print "You did not enter a four digit number"
        return False
    #Check if not number?
    return True


def check_guess(num, rand_int):
    new_num = ""
    cows = 0
    count1 = 0
    for i in num:
        if str(i) == str(rand_int[count1]):
            new_num += ""
            cows += 1
        else:
            new_num = new_num + rand_int[count1]
        count1 += 1
    print cows
    print new_num

    bulls = 0
    for i in new_num:
        for j in num:
            if str(i) == str(j):
                bulls += 1
    print bulls

    return str(cows) + " cow(s) " + str(bulls) + " bull(s)"


# def game_won(num_cows):
#     if num_cows == 4:
#         return True


####################################################


print "Welcome to the Cows and Bulls Game!"
print ""
print "Guess the random four digit number by receiving a cow\n" \
      "for every digit that you guess correctly in the correct\n" \
      "place and a bull if it is not a cow you guess correctly,\n" \
      "but in the wrong place. Good luck!"
print ""

# while (game_won)
user_num = raw_input("Enter a four digit number: ")

while error_check(user_num) == 0:
    user_num = raw_input("Enter a four digit number: ")

print check_guess(user_num, rand_number)