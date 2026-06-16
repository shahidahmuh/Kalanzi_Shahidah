TotalBillAmount = float(input("Enter your Total Bill Amount:"))
NumberOfPeople = int(input("Enter the Number of People:"))
print("\n TipPercentage options")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. custom")

choice = input("Choose a Tip Percentage (1-4):")

if choice == '1':
    TipPercentage = 10
elif choice == '2':
    TipPercentage = 15 
elif choice == "3":
    TipPercentage = 20
elif choice == "4":
    TipPercentage = float(input("Enter custom tip percentage:"))
else:
    print("Invalid choice.")
    TipPercentage=10

TipAmount = TotalBillAmount * TipPercentage/100
TotalBill = TotalBillAmount + TipAmount
AmountperPerson = TotalBill / NumberOfPeople
#results display
print("\nRECEIPT")
print(f"Bill Amount: {TotalBillAmount:,.2f}")
print(f"Tip Percentage: {TipPercentage}%")
print(f"Tip Amount: {TipAmount:,.2f}")
print(f"Total Bill: {TotalBill:,.2f}")
print(f"number of People: {NumberOfPeople}")
print(f"Amount Per Person: {AmountperPerson:,.2f}")
