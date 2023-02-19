#Challenge #009 --> 29/12/2022

'''

Write a program that will ask for a number of days
and then will show how many hours, minutes and seconds
are in that number of days.

'''

Days = int(input("How many days? "))

Hours = Days * 24

Minutes = Hours // 60

Seconds = Minutes // 60

print("There are",Hours, "hours", Minutes, "minutes", Seconds, "seconds")



input()


#took 2 tries but slight error in minutes in some examples :/
