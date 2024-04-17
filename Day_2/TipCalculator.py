print("Welcome to the tip calculator!\n")
TotalBill=input("What was the total bill? $\n")
tip=float(input("How much tip would you like to give?\n")) /100
consumers=input("How many people to split the bill?\n")
billPerPerson= (float(TotalBill) / float(consumers))
billWithTip= billPerPerson * (1+tip)
print(f"Each person should pay: ${billWithTip:.2f}")
