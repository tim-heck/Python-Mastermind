#################################
# Mastermind python mini project
# Tim Heck
# 02/23/16
# User enters a four digit number to try to guess the
# randomly generated four digit number, cows are
# counted if a digit correctly matches the specific place
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

print rand_number

####################################################


# Method to check if the user entered number is
# a four digit number
def error_check(n):
    if len(n) < 4 or len(n) > 4:
        print "You did not enter a four digit number"
        return False
    # Check if not number?
    return True


# Method for comparing the user guess with the randomly
# generated number. Counts the number of cows and the number
# of bulls
def compare_guess(num, rand_int):
    new_num = ""  # The new number with removed cows
    # new_num = []
    cows = 0
    count1 = 0
    # Checks each digit from user enter number with the
    # randomly generated number for correct position
    # counts the cows, if a cow is found, that digit from
    # the user entered number is removed
    for i in num:
        if str(i) == str(rand_int[count1]):
            new_num += "E"
            # new_num.append("E")
            cows += 1
        else:
            new_num += rand_int[count1]
            # new_num.append(num[count1])
        count1 += 1

    print new_num

    bulls = 0
    # Checks each digit of the new number with each digit
    # in the randomly generated number to count bulls
    for i in range(0, len(new_num)):
        for j in range(0, 4):
            if str(new_num[i]) == str(num[j]):
                bulls += 1
                new_num = new_num[:i] + "E" + new_num[i+1:]
                # Eliminates double counting for bulls for multiple numbers
                # if bulls == (bulls - 1) + 1:
                break
    print new_num

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
