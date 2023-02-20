"""
Ask the user to enter a number. If it is under 10, 
display the message “Too low”, if their number is 
between 10 and 20, display “Correct”, otherwise 
display “Too high”.
"""

Num = int(input("Enter a number: "))

if Num <= 9:
    print("Too low")
elif Num == 10 or Num <= 20:
    print("Correct")
else:
    print("Too high")



input()


#took 5 tries! :)
