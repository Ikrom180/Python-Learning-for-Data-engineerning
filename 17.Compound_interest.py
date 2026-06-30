#Python compound interest calculator

# A = P(1 + r/n)^t

principal = 0
rate = 0
time = 0

while True :
    principal = float(input("Enter the principal amount: "))
    if principal < 0 :
        print('principal amount cannot be less than zero')
    else :
        break
while True :
    rate = float(input("Enter the interest rate : "))
    if principal < 0 :
        print('rate  cannot be less than zero')
    else :
        break
while True :
    time = float(input("Enter the time : "))
    if principal < 0 :
        print('time  cannot be less than zero')
    else :
        break

# print(principal)
# print(rate)
# print(time)


total= principal * pow((1 + rate / 100), time)
print(total)

print(f"Balance after {time} year/s: ${total:2.f}")