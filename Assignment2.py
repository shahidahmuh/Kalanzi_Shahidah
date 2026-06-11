attempts = 3 
while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == "Admin" and password == "12345":
        role = "admin"
        break
    elif username == "Cashier" and password =="02468":
        role = "cashier"
        break
    elif username == "Customer" and password == "13579":
        role = "customer"
        break
    else :
        attempts -= 1
        print(f"Invalid Creentials. Attempts left {attempts}")

if attempts == 0:
    print("Maximum login attempts reached.")
else:
    print(f"\n Welcome {role}")    

    if role == "cashier":
        print("Access: Sales")
        print("Process Customer purchases.")
    elif role == "admin":
        print("Access: Full Access")
        print("Manage Products and Users")
    elif role ==  "customer":
        print("Access: Shopping")
        print("Buy Products")

    print ("\n E-Commerce Calculator")
    
    subtotal = float(input("Enter product Subtotal:"))
    coupon = input("Enter Coupon Code:")

    if coupon == "C001":
        discount_rate = 10
    elif coupon == "C002":
        discount_rate = 30
    elif coupon == "C003":
        discount_rate = 20
    else:
        discount_rate = 0
        print("Invalid Coupon Code")
    
    discount = subtotal * discount_rate/100
    amount_after_discount = subtotal - discount
    tax_rate = float(input("Enter Tax Rate(%):"))
    tax = amount_after_discount * tax_rate/100
    final_price = amount_after_discount + tax

    print("\n RECEIPT")
    print(f"Role : {role}")
    print(f"Subtotal : {subtotal}")
    print(f"Discount Rate : {discount_rate}%")
    print(f"Discount Amount : {discount}")
    print(f"Tax Rate : {tax_rate}%")
    print(f"Tax Amount : {tax}")
    print(f"Final Price : {final_price}")