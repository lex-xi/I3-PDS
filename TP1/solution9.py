def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    bill = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)

    bill = bill + 2000      # service fee
    bill = bill * 1.10      # VAT 10%

    return round(bill)


# (b)
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh} kWh -> {bill:,} riel (≈ {usd:.2f} USD)")


# (c)
kwh = float(input("Enter your monthly consumption (kWh): "))

bill = electricity_bill(kwh)

if bill is None:
    print("Invalid consumption")
else:
    print(f"Your bill is {bill:,} riel")