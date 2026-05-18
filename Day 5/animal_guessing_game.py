"""
Inputs: 
A string containing an attribute guess or the guesso f the animal's name.

Processes:
-Randomly select an animal.
-Allow the user to guess until they guess the correct animal.
-When they guess, tell them if the animal has the attribute or not.
-Tell the user when they guess correctly.

Outputs:
-Attribute guess correctness
-Congratulations message

"""

import random  # teach python how to do random stuff

ANIMALS = {
"Lion" : ["Mammal", "Four legs", "Predator", "Coat", "Golden", "Roars", "Strong"],
"Hyena" : ["Mammal", "Four legs", "Predator", "Spots", "Laughs", "Wild", "Fast"],
"Elephant": ["Mammal", "Large", "Trunk", "Gray", "Heavy", "Tusks", "Wrinkled"],
"Tiger": ["Mammal", "Stripes", "Predator", "Orange", "Fierce", "Fast", "Sharp teeth"],
"Giraffe": ["Mammal", "Tall", "Spots", "Long neck", "Yellow", "Gentle", "Long legs"],
"Zebra": ["Mammal", "Stripes", "Four legs", "Black and white", "Fast", "Wild", "Herds"],
"Penguin": ["Bird", "Black and white", "Swims", "Cold", "Waddles", "Flippers", "Cute"],
"Crocodile": ["Reptile", "Scales", "Predator", "Water", "Teeth", "Green", "Dangerous"],
"Kangaroo": ["Mammal", "Jumps", "Pouch", "Australia", "Strong legs", "Tail", "Fast"],
"Panda": ["Mammal", "Black and white", "Fluffy", "Bamboo", "Cute", "Lazy", "Round"]
    }

WELCOME_MESSAGE = """
Welcome to the Animal Guessing Game!
I have selected a random animal from my list.
Guess an attribute or the name of the animal.
"""

CONGRATULATIIONS_MESSAGE = "You won!"

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]
print(WELCOME_MESSAGE)

guess = ""
while guess != random_animal:
    guess = input("Please guess an attribute or an animal name: ").capitalize()
    if guess in random_animal_attributes: 
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATULATIIONS_MESSAGE)
    else:
        print(f"No, {guess} is NOT an attribute of the animal.")


