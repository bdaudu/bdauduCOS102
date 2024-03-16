principal = input("Enter in the principal ")
principal = float(principal)

rate = input("Enter in the rate ")
rate = int(rate)

time = input("How many years? ")
time = int(time)

rt = (rate * time)/100

a = principal * (1 + rt)
print("The amount for simple interest is ₦" + str(a))

n = input("How many times is interest credited to ypur account per annum? ")
n = int(n)

power = n * time
x = (1 + (rate/n)) ** (power)

a2 = principal * x
print("The amount for compound interest is ₦" + str(a2))

M = input("Lastly, input your M ")
M = int(M)

T = input("and the T ")
T = int(T)

d = rate/n

a3 = principal * M * T * ((x-1)/d)
print("The amount for annuity plan is ₦" + str(a3))



