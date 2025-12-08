rates = {
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0096
}

amount = float(input("Enter amount in INR: "))

print("USD:", round(amount * rates["USD"], 2))
print("EUR:", round(amount * rates["EUR"], 2))
print("GBP:", round(amount * rates["GBP"], 2))
