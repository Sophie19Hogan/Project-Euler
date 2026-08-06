#Problem 2
total = 0
start = 1
a = 1
b = a + start
while a < 4000000 and b < 4000000:
    if a % 2 == 0:
        total = total + a
    elif b % 2 == 0:
        total = total + b
    a = a + b
    b = a + b
print(f"The sum is {total}.")

