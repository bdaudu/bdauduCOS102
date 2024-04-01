op = int(input("Welcone to our root calculator. Pick from operations 1 to 3 "))

if op == 1:
    print("Your operation is the roots of a quadratic equation: ax^2 + bx + c = 0")
    a = int(input("Enter in the first coefficient: "))
    b = int(input("Enter in the second coefficient: "))
    c = int(input("Enter in the third coefficient: "))

    f_r = -b/a
    s_r = c/a

    print(f"The roots for this equation are {f_r} and {s_r}",)

elif op == 2:
    print("Your operation is the roots of a cubic equation: ax^3 + bx^2 + cx + d = 0")
    a2 = int(input("Enter in the first coefficient: "))
    b2 = int(input("Enter in the second coefficient: "))
    c2 = int(input("Enter in the third coefficient: "))
    d = int(input("Ehter in the fourth coefficient: "))

    f_r2 = -b2/a2
    s_r2 = c2/a2
    t_r = -d/a2

    print(f"The roots for this equation are {f_r2}, {s_r2} and {t_r}",)

elif op == 3:
    print("Your operation is the roots of a quartic equation: ax^4 + bx^3 + cx^2 + dx + e = 0")
    a3 = int(input("Enter in the first coefficient: "))
    b3 = int(input("Enter in the second coefficient: "))
    c3 = int(input("Enter in the third coefficient: "))
    d2 = int(input("Ehter in the fourth coefficient: "))
    e = int(input("Enter in the last term: "))


    f_r2 = -b3/a3
    s_r2 = c3/a3
    t_r2 = -d2/a3
    ft = e/a3

    print(f"The roots for this equation are {f_r2}, {s_r2}, {t_r2} and {ft}",)

else:
    print("There are no more operations apart from operations 1, 2 and 3") 