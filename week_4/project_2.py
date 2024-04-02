info = input("Welcome, fellow staff, to the Izifin Technology Experience App. What is your name, please? ")
sur = input("Enter your surname too. ")
print("\n")
years = float(input("How many years of experience do you have in Fintech? "))
print("\n")
age = int(input("How old are you? "))

if years >= 25 and age >= 55:
    print(f"{info} {sur}, your annual tax revenue(ATR) is N5,600,000")
elif years >= 20 and age >= 45:
    print(f"{info} {sur}, your annual tax revenue(ATR) is N4,480,000")
elif years >= 10 and age >=35:
    print(f"{info} {sur}, your annual tax revenue(ATR) is N1,500,000")
else:
    print(f"{info} {sur}, your annual tax revenue(ATR) is N550,000")