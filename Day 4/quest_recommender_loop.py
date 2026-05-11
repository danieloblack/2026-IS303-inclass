'''

inputs:
-player class (string)
-player level (integer)

processes:
Suggests a quest type based on player level and class
Different quests for level ranges (1-10, 11-25, 26+),
modified by class (warrior, mage, rogue)

outputs:
print a recommended quest

'''

class_types = {
    "Wizard" : ["Find a wand", "Find a spellbook", "Duel your professor"],
    "Figher" : ["Find a sword", "Find a shield", "Defend your professor"]
}


quest_to_find = input("What quest do you want? ")

for class_key in class_types:
    class_quests = class_types[class_key]
    for quest in class_quests:
        if quest == quest_to_find:
            print(f"{quest} is a quest for the {class_key} class.")


player_class = input("What is your class? ").capitalize()
player_level = ""
while not player_level.isdigit():
    player_level = input("What is your current level? (enter a number) ")

quest_level = 0
if quest_level >= 26:
    quest_level = 2
elif quest_level >= 11:
    quest_level = 1

recommeneded_quest = class_types[player_class][quest_level]
print(f"You should do this quest: {recommeneded_quest}")

users_class_quests = class_types[player_class]
print(users_class_quests)
quest_by_level = users_class_quests[quest_level]
print(quest_by_level)

