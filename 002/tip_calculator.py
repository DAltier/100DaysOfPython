#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

amount_per_person = "{:.2f}".format(float(bill) / int(people) * float((100 + int(tip))/100), 2)
print(f"Each person should pay: ${amount_per_person}")