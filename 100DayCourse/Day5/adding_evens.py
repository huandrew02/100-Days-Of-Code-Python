total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total += n
print(total)

# or
total2 = 0
for i in range(2, 101, 2):
    total2 += i
print(total2)