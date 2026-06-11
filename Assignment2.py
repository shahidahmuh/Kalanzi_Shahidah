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
       