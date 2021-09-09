
print("GROSS PAY CALCULATION OF GIVEN BASIC PAY")
BP=float(input("Enter Basic Pay :"))
DA=float(BP*0.40)
HRA=float(BP*0.20)
GROSSPAY=float(BP+DA+HRA)

print(" BASIC PAY : ",BP)
print(" DEARNESS ALLOW. : ",DA)
print(" HOUSE RENT ALLOW.: ",HRA)
print(" GROSS PAY : ",GROSSPAY)