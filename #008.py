#Challenge #008 --> 29-12-2022

'''

Ask for the total price of the bill,
then ask how many diners there are.

Divide the total bill by the number of diners
and show how much each person must pay.

'''

TPrice = int(input("What is the total price of the bill? "))

NDiners = int(input("How many diners are there? "))

Payment = TPrice//NDiners

print("Each person must pay", Payment)



input()

#Took 2 tries!
