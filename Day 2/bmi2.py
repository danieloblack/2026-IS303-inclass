"""

Inputs
- name
- height
- weight
- age
- sex

Processes
- Input validation
- Calculate BMI using the formula: weight / [height ^2 x 703
- Categorize BMI
    - underweight: < 18.5
    - healthy: 18.5-24.9
    - overweight: 25,0-29.9
    - obese: 30-39.9
    - severe obese: 40+

Outputs
- Report for the user with their BMI and category

"""
#Collect Inputs
name = input("Name: ")
age = input("Age: ")
sex = input("Sex: ")
height = input("Height (inches): ")
weight = input("Weight (pounds): ")

#Input validation
age = age.replace(".", "",1)
age_is_int = age.isdigit()
age_is_reasonable = True
if age_is_int == True:
    age = int(age)
age_is_reasonable = False
if age_is_int == True and age < 140 and age > 1:
    age_is_reasonable = True

sex = sex.lower()
sex_is_valid = False
if sex == "male" or sex == "female":
    sex_is_valid = True

height = height.replace(".", "",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int == True and height >= 12 and height <= 140:
    height_is_reasonable = True

weight = weight.replace(".", "",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int == True and weight >= 12 and weight <= 1200:
    weight_is_reasonable = True

ready_to_process = True

if age_is_int == False or age_is_reasonable == False:
    print("You entered a non-expected age, please use whole numbers.")
else:
    age = int(age)  
    ready_to_process = False

if sex_is_valid == False:
    print("You entered a non-expected sex, please enter Male or Female.")
    ready_to_process = False
    
if height_is_int == False or height_is_reasonable == False:
    print("You entered a non-expected height in inches, please use whole numbers between 12 and 140.")
    ready_to_process = False

if weight_is_int == False or weight_is_reasonable == False:
    print("You entered a non-expected weight in pounds, please use whole numbers between 12 and 1200.")
    ready_to_process = False
if ready_to_process == True:
    bmi = weight / (height ** 2) * 703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_category = "healthy"
    elif bmi >= 25.0 and bmi <= 29.9:
        bmi_category = "overweight"         
    elif bmi >= 30 and bmi <= 39.9:
        bmi_category = "obese"
    else:
        bmi_category = "severely obese" 

    # Report
    print(f"Report for {name}:")
    print(f"Age: {age} years old")
    print(f"Your BMI is {bmi}")
    print(f"Your BMI category is: {bmi_category}")