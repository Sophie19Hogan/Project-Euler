#Problem 0
n = 1
total = 0
for i in range (214000):
    square = n**2
    if square % 2 != 0:
        total = total + square
    n = n + 1
print(f"The sum of the odd squares is {total}.")