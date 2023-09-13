from decimal import Decimal as D

sum = 0
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print(sum)

print("The actual result of the operation below is supposed to be zero")

print("0.1 + 0.1 + 0.1 - 0.3 = ", 0.1 + 0.1 + 0.1 - 0.3) 


