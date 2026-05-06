age = input("Age: ")
if int(age)<0:
    print("Invalid age")
elif int(age)<18:
    print("Minor")
else:
    print("Adult")
    