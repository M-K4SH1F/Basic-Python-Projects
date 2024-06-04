print("Welcome to the tip calculator!")

#The user enters the total amount of the bill. 
bill = float(input("What was the total bill? $\n"))

#The user enters the amount of tip they like to give from 1,2,5 to 10.
tip = int(input("How much tip would you like to give? 1, 2, 5, or 10?\n"))

#Number of people the amount is split into.
people = int(input("How many people to split the bill?\n"))

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")