print("Welcome to the tip calculator!\n")
bill=float(input("What was the total bill? $"))
tip=float(input("How much tip would you like to give?\n")) /100
people=int(input("How many people to split the bill?\n"))
billPerPerson= (float(bill) / float(people))
billWithTip= billPerPerson * (1+tip)
print(f"Each person should pay: ${billWithTip:.2f}")
