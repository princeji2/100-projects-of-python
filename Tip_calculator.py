print("Welcome MY friend! in our tip calculation!")
total_bill = float(input("Please enter the total bill amount: \n"))
tip_percentage = float(input("Please enter the tip percentage you would like to give (e.g., 15 for 15%): \n"))
people = int(input("Please enter the number of people to split the bill: \n"))

tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount
print(f"The total bill amount including tip is : ${total_amount:.2f}")
amount_per_person = total_amount / people

print(f"Each person should pay: ${amount_per_person:.2f}")
print("Thank you for using the Tip Calculator!")
