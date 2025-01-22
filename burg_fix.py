principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print(f"principal cannot be less than zero")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print(f"rate cannot be less than zero")
    else:
        break


while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print(f"time cannot be less zero")
    else:
        break


total = principal * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s is: ${total:.2f}")