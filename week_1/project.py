principal = input("Enter in the principal for simple interest ")
principal = float(principal)

rate = input("Enter in the rate ")
rate = int(rate)

time = input("How many years? ")
time = int(time)

rt = (rate * time)/100

a = principal * (1 + rt)
print("The amount for simple interest is ₦" + str(a))

n = input("How many times is interest credited to your account per annum? ")
n = int(n)

principal2 = input("Enter in the principal for compound interest ")
principal2 = float(principal2)

rate2 = input("Enter in the rate for compund interest ")
rate2 = int(rate2)

time2 = input("How many years for C.I.? ")
time2 = int(time2)

power = n * time2
x = (1 + (rate2/n)) ** (power)

a2 = principal2 * x
print("The amount for compound interest is ₦" + str(a2))

pmt = input("Lastly, enter in the period cash payment")
pmt = float(pmt)

n2 = input("How many times is interest credited to your account per annum? ")
n2 = int(n2)

principal3 = input("Enter in the principal ")
principal3 = float(principal3)

rate3 = input("Enter in the rate ")
rate3 = int(rate3)

time3 = input("How many years for the annuity plan? ")
time3 = int(time3)

power2 = n2 * time3
x2 = (1 + (rate3/n2)) ** (power2)

d = rate3/n2

a3 = pmt * ((x2-1)/d)
print("The amount for annuity plan is ₦" + str(a3))



