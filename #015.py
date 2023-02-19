
# Ask the user to enter their favourite colour.

# If they enter "red", "RED" or "Red"
# display the message "I like red too",
# otherwise display the message
# "I don't like [colour], I prefer red".

print("What is your favourite colour? ")

colour = input()
colour.lower()

if colour == "red":
    print("I like red too")
else:
    print("I don't like ", colour, ", I prefer red")

input()
