
# Ask the user to enter a number that is under 20.

# If they enter a number that is 20 or more,
# display the message "Too high", otherwise display "Thank you"

print ("Enter a number that is under 20: ")

num = int(input())

if num > 20:
    print("Too high")
else:
    print("Thank you")

input()


# also tok less than 5 tries.

# the issue was int(input()) not input(int()), silly ik
