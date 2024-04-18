admitted_mc = []
not_admitted_mc = []
admitted_cs = []
not_admitted_cs = []

def mass_comm():
    number1 = int(input("How many people are applying for this course? "))
    for i in range(number1):
        name1 = str(input("What is your name? "))
        jamb1 = int(input("What was your score in JAMB?"))
        interview1 = str(input("Did you pass the interview? "))
        grade = str(input(f"What grade do you get in Math? "))
        grade_2 = str(input("In English? "))
        grade_3 = str(input("In Literature? "))
        grade_4 = str(input("In Civic? "))
        grade_5 = str(input("In History? "))

    if jamb1 >= 230 and interview1 == "yes" and grade == "A" or "B" or "C":
        not_admitted_mc.append(name1)
        return not_admitted_mc
    elif jamb1 >= 230 and interview1 == "yes" and grade_2 == "A" or "B" or "C":
        not_admitted_mc.append(name1)
        return not_admitted_mc
    elif jamb1 >= 230 and interview1 == "yes" and grade_3 == "A" or "B" or "C":
        not_admitted_mc.append(name1)
        return not_admitted_mc
    elif jamb1 >= 230 and interview1 == "yes" and grade_4 == "A" or "B" or "C":
        not_admitted_mc.append(name1)
        return not_admitted_mc
    elif jamb1 >= 230 and interview1 == "yes" and grade_5 == "A" or "B" or "C":
        not_admitted_mc.append(name1)
        return not_admitted_mc
    else:
        admitted_mc.append(name1)
        return admitted_mc


def comp_sci():
    number2 = int(input("How many people are applying for this course? "))
    for i in range(number2):
        name2 = str(input("What is your name? "))
        jamb2 = int(input("What was your score in JAMB?"))
        interview2 = str(input("Did you pass the interview? "))
        grade = str(input("What grade do you get in Math? "))
        grade_2 = str(input("In English? "))
        grade_3 = str(input("In Chemistry? "))
        grade_4 = str(input("In Physics? "))
        grade_5 = str(input("In Data Processing? "))

    if jamb2 >= 230 and interview2 == "yes" and grade == "A" or "B" or "C":
        not_admitted_cs.append(name2)
        return not_admitted_cs
    elif jamb2 >= 230 and interview2 == "yes" and grade_2 == "A" or "B" or "C":
        not_admitted_cs.append(name2)
        return not_admitted_cs
    elif jamb2 >= 230 and interview2 == "yes" and grade_3 == "A" or "B" or "C":
        not_admitted_cs.append(name2)
        return not_admitted_cs
    elif jamb2 >= 230 and interview2 == "yes" and grade_4 == "A" or "B" or "C":
        not_admitted_cs.append(name2)
        return not_admitted_cs
    elif jamb2 >= 230 and interview2 == "yes" and grade_5 == "A" or "B" or "C":
        not_admitted_cs.append(name2)
        return not_admitted_cs
    else:
        admitted_cs.append(name2)
        return admitted_cs


course = str(input("Welcome to the portal for Computer Science/Mass Communication Admission\nPlease input the course: "))

if course == "Computer Science":
    comp_sci()
elif course == "Mass Communication":
    mass_comm()
else:
    print("Only Computer Science and Mass Communication are on this portal")

print(f"These students are qualified to do Mass Communciation: {admitted_mc}")
print(f"These students are not qualified to do Mass Communciation: {not_admitted_mc}")

print("\n")

print(f"These students are qualified to do Computer Science: {admitted_cs}")
print(f"These students are not qualified to do Computer Science: {not_admitted_cs}")





