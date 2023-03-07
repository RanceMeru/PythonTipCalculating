#This is a program to calculate a tip
#
#Get the amount of the bill
bill_amount = float(input("What is the total bill amount? "))

#Get the percentage of the tip
tip_percent = float(input("What percentage tip would you like to leave? "))

#Calculate the tip amount
tip_amount = bill_amount * (tip_percent/100)

#Calculate the total amount
total_amount = bill_amount + tip_amount

#Print the result
print("The tip amount is $" + str(round(tip_amount,2)))
print("The total amount is $" + str(round(total_amount,2)))
