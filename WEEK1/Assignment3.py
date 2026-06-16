print("WORLD CUP 2026 PREDICTION")

while True:
    country = input("\nEnter a country or 'quit' to stop:")

    if country.lower()== "quit":
        print("Program ended.")
        break
    if country == "":
        print("Please enter a country name:")
        continue
    if country.lower() == "portugal":
        pass
    if country.lower() == "argentina":
        print("High chance of winning")
    elif country.lower() == "france":
        print("High chance of winning")
    elif country.lower() =="brazil":
        print("High chance of winning")
    else:
        print("Prediction recorded")