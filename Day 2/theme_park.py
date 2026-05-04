"""

Inputs:
-Age
-Day of the week
-height
-VIP
-Signed waiver
-Parent Present

Processes:
-Use the variables to identify which rides are available.

Outputs:
-A list of rides

"""

age = int(input("Age: "))
day_of_week = input("Day of the week: ")
height = int(input("Height in inches: "))
vip = input("VIP? yes/no").lower()
signed_waiver = input("Signed waiver? yes/no").lower()
parent_present = input("Parent present? yes/no").lower()

# MegaDrop
if age>= 14 and signed_waiver == "yes" and height >= 54 or (vip == "yes" and height >= 50):
    print("MegaDrop")

# thunderBolt
if age >= 10 and height >= 48 and day_of_week != "Monday":
    print("Thunderbolt")    

# Kiddie
if age > 8 or parent_present == "yes":
    print("Kiddie")
    ride_found = True

    if ride_found == False:
        print("No ride found")
        





