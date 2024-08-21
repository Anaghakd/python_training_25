#Program to check if user given year is a leap year
year=int(input('Enter a year:'))
if year %4 == 0:
    print("The user given year is a leap year")
else:
    print("The user given year is not a leap year")
