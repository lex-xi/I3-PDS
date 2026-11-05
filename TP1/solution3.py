# Function: Celsius to Fahrenheit
def celsius_to_fahrenheit(c, round_to=1):
    f = c * 9 / 5 + 32
    return round(f, round_to)

# Function: Fahrenheit to Celsius
def fahrenheit_to_celsius(f, round_to=1):
    c = (f - 32) * 5 / 9
    return round(c, round_to)


# (a) Conversion table
print("°C | °F")
print("------+-------")

for c in range(0, 101, 20):
    print(c, "|", celsius_to_fahrenheit(c))

# (b) Convert 98.6°F to Celsius
print("\n98.6 °F =", fahrenheit_to_celsius(98.6), "°C")

# (c) Convert 37°C to Fahrenheit and back
f = celsius_to_fahrenheit(37)
c = fahrenheit_to_celsius(f)

print("37 °C =", f, "°F")
print(f, "°F =", c, "°C")

# (d) round_to = 3
print("\n37 °C =", celsius_to_fahrenheit(37, round_to=3), "°F")

print("\nDefault argument is useful because")
print("we can use 1 decimal place automatically")
print("and only change it when needed.")