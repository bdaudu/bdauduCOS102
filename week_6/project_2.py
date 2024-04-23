admitted = []
not_admitted = []



def mass_comm():
    number1 = int(input("How many people are applying for this course? "))
    for i in range(number1):
        name1 = str(input("What is your name? "))
        jamb1 = int(input("What was your score in JAMB?"))
        interview1 = str(input("Did you pass the interview? "))
        grade = ["A", "B", "C", "a", "b", "c"]
        s_mc1 = str(input("What grade did you get in Mathematics? "))
        s_mc2 = str(input("What grade did you get in English Language? "))
        s_mc3 = str(input("What grade did you get in Literature? "))
        s_mc4 = str(input("What grade did you get in Civic? "))
        s_mc5 = str(input("What grade did you get in History? "))
    
        if jamb1 >= 230 and interview1 == "yes" and s_mc1 in grade and s_mc2 in grade and s_mc3 in grade and s_mc4 in grade and s_mc5 in grade:
            admitted.append(name1)
        else:
            not_admitted.append(name1)


def comp_sci():
    number2 = int(input("How many people are applying for this course? "))
    for i in range(number2):
        name2 = str(input("What is your name? "))
        jamb2 = int(input("What was your score in JAMB?"))
        interview2 = str(input("Did you pass the interview? "))
        grade = ["A", "B", "C", "a", "b", "c"]
        s_cs1 = str(input("What grade did you get in Mathematics? "))
        s_cs2 = str(input("What grade did you get in English Language? "))
        s_cs3 = str(input("What grade did you get in Chemistry? "))
        s_cs4 = str(input("What grade did you get in Physics? "))
        s_cs5 = str(input("What grade did you get in Data Processing? "))
            
        if jamb2 >= 250 and interview2 == "yes" and s_cs1 in grade and s_cs2 in grade and s_cs3 in grade and s_cs4 in grade and s_cs5 in grade:
            admitted.append(name2)
        else:
            not_admitted.append(name2)
    

course = str(input("Welcome to the portal for Computer Science/Mass Communication Admission\nPlease input the course: "))

if course == "Computer Science":
    comp_sci()
elif course == "Mass Communication":
    mass_comm()
else:
    print("Only Computer Science and Mass Communication are on this portal")


print(f"Admitted Students:{admitted}")
print(f"Non-Admitted Students:{not_admitted}")

