# (a)
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# (b)
def days_in_month(month, year):
    if month < 1 or month > 12:
        return None
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


# (c)
years = [1900, 2000, 2024, 2026]

for year in years:
    if is_leap(year):
        print(year, "leap")
    else:
        print(year, "not leap")

print("Feb 2024:", days_in_month(2, 2024))
print("Feb 2026:", days_in_month(2, 2026))
print("Apr:", days_in_month(4, 2026))
print("month 13:", days_in_month(13, 2026))


# (d)
count = 0

for year in range(2000, 2101):
    if is_leap(year):
        count += 1

print("Leap years from 2000 to 2100:", count)