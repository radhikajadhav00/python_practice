numbers = [12, 7, 5, 64, 14, 27, 90, 33]

evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Even numbers:", evens)
print("Odd numbers:", odds)
