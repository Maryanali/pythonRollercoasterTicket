#!/usr/bin/env python3
#Python Day 3:

#conditional statements with comparison operators 
#exercise 1- Rollercoaster

print("Welcome to the rollercoaster ride! 🙂")
height = int(input("Input your height in cm: "))

if height >= 120:
	print("You can ride this rollercoaster!! 🎇")
else:
	print("Sorry you cannot ride the rollercoaster 😔")
	

#exercise 3- Rollercoaster prices: Nested if statements and if else statements
#nested if else statement is a if statement inside another if statement 	

bill = 0
if height >= 120:
	print("You can ride the rollercoaster")
	age = int(input("What is your age?"))
	if age < 12:
		bill = 5
	elif age < 18 :
		bill = 10
	elif age > 60:
		bill = 5
	else: 
		bill = 12
	
	wants_photo = input("Do you want a photo taken, Y or yes or N for no ")
	if wants_photo == "Y" or "y":
		bill += 3
	print(f"Your final bill is {bill}")
		
else:
	print("Sorry you cannot ride the rollercoaster")