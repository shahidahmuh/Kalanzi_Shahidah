class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        print()
restaurant = Restaurant("The Food Place", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

Restaurant1 = Restaurant("Shawarma Place", "Middle Eastern")
Restaurant2 = Restaurant("Spice Hub", "Indian")
Restaurant3 = Restaurant("Sushi Place", "Japanese")
Restaurant1.describe_restaurant()
Restaurant2.describe_restaurant()
Restaurant3.describe_restaurant()
