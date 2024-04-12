#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.6
print("Welcome to the tip calculator")
bill=float(input("What is your total bill ? $"))
tip=int(input("How much tip would you like to give ? 12, 15, 18, 20? "))
persons=int(input("How many persons to split into bill ?"))

tip_percentage=tip/100
total_tip=bill*tip_percentage
total_bill=bill+total_tip
bill_per_person=total_bill/persons
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")