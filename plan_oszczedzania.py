# Plan oszczędzania

month_savings = 440
months_in_year = 12
years = 5
year_bonus = 500

year_amount = month_savings * months_in_year
year_with_bonus = year_amount + year_bonus
five_years_with_bonus = year_with_bonus * years
five_years_without_bonus = year_amount * years

print("Po roku oszczędzania uzbieram:", year_amount, "zł")
print("Z coroczną premią:", year_with_bonus, "zł")
print("Po 5 latach z premiami:", five_years_with_bonus, "zł")
print("Po 5 latach bez premii:", five_years_without_bonus, "zł")
