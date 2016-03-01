#################################
# Mastermind python mini project
# Tim Heck
# 02/23/16
# User enters a four digit number to try to guess the
# randomly generated four digit number, cows are
# counted if a digit correctly matches the digit and place
# and a bull if a digit correctly matches but is not in
# the correct place
#################################

from random import randint

# Creates random four digit number as a string
rand_number = ""
count = 0
while count < 4:
    rand_number += str(randint(0, 9))
    count += 1

####################################################


# Method to check if the user entered number is
# a four digit number
def error_check(n):
    if len(n) < 4 or len(n) > 4:
        print "You did not enter a four digit number"
        return False
    return True


# Method for comparing the user guess with the randomly
# generated number. Counts the number of cows and the number
# of bulls
def compare_guess(num, rand_int):
    cows = 0
    bulls = 0
    # Checks each digit from user enter number with the
    # randomly generated number for correct position then
    # counts the cows, if a cow is found, that digit from
    # the user entered number is replaced with a 'c' and
    # randomly generated digit is replaced with a 'C'
    for i in range(0, 4):
        if str(rand_int[i]) == str(num[i]):
            rand_int = rand_int[:i] + "C" + rand_int[i+1:]
            num = num[:i] + "c" + num[i+1:]
            cows += 1

    # Checks each digit of the rand_int, including any cows found,
    # with each digit in the user entered number to count bulls
    # if a bull is found, the digit from the user entered number
    # is replaced with a 'b' and randomly generated digit is
    # replaced with a 'B'
    for i in range(0, 4):
        for j in range(0, 4):
            if str(rand_int[i]) == str(num[j]):
                bulls += 1
                rand_int = rand_int[:i] + "B" + rand_int[i+1:]
                num = num[:j] + "b" + num[j+1:]  # Prevents a single digit to be double counted
                break

    return str(cows) + " cow(s), " + str(bulls) + " bull(s)"

####################################################

print ""
print "Welcome to the Cows and Bulls Game!"
print ""
print "Guess the randomly generated four digit number by receiving a\n" \
      "cow for every digit that you guess correctly in the correct\n" \
      "place, and a bull if it is not a cow you and if you guess\n" \
      "correctly, but in the wrong place. Good luck!"
print ""

user_num = 1
num_guesses = 0

# Executes until the user enter number correctly matches
# the randomly generated number
while rand_number != user_num:
    user_num = raw_input("Enter a four digit number: ")

    while error_check(user_num) == 0:
        user_num = raw_input("Enter a four digit number: ")

    print compare_guess(user_num, rand_number)
    num_guesses += 1

print "You win! It took you " + str(num_guesses) + " guess(es)."
