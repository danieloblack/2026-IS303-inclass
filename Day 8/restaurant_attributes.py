class Restaurant:
    def __init__(self, name, location, hours):
        self.name = name
        self.location = location
        self.hours = hours
        self.menu = []
        self.reviews = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def add_review(self, review):
        self.reviews.append(review)

    def average_price(self):
        if len(self.menu) == 0:
            return 0

        total = 0

        for item in self.menu:
            total += item.price

        return round(total / len(self.menu), 2)

    def __str__(self):
        return (
            f"{self.name} is located at {self.location}. "
            f"It is open {self.hours}. "
            f"It has {len(self.menu)} menu items and "
            f"{len(self.reviews)} reviews. "
            f"The average menu price is ${self.average_price()}."
        )


class MenuItem:
    def __init__(self, name, price, category, calories, ingredients):
        self.name = name
        self.price = price
        self.category = category
        self.calories = calories
        self.ingredients = ingredients

    def __str__(self):
        return (
            f"{self.name} ({self.category}) costs ${self.price} "
            f"and has {self.calories} calories."
        )


# Create restaurants
restaurant_1 = Restaurant(
    "Wing Stop",
    "123 Main Street",
    "10 AM - 11 PM"
)

restaurant_2 = Restaurant(
    "Blue Line Deli",
    "BYU Campus",
    "8 AM - 8 PM"
)


# Create menu items
wings = MenuItem(
    "Original Chicken Wings",
    6.99,
    "Entree",
    1000,
    ["Chicken Wings", "Buffalo Sauce", "Ranch"]
)

sandwich = MenuItem(
    "Turkey Sandwich",
    10.99,
    "Entree",
    500,
    ["Turkey", "Lettuce", "Tomato", "Mayo"]
)


# Add items to menus
restaurant_1.add_menu_item(wings)
restaurant_2.add_menu_item(sandwich)


# Add reviews
restaurant_1.add_review("The wings are amazing!")
restaurant_1.add_review("Great sauces!")

restaurant_2.add_review("Fresh sandwiches and good service.")


# Print restaurant info
print(restaurant_1)
print()

print(restaurant_2)
print()


# Print menu items
for item in restaurant_1.menu:
    print(item)

print()

for item in restaurant_2.menu:
    print(item)