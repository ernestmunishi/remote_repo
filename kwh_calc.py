# There is updates to make
# To calculate the amount of electricity used per month,
# week, day, hour, minute, and per second.

from datetime import date

total_units = float(input("The total amount of units entered: "))
print("THE DATE UNITS(kwh) WERE ENTERED")
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

date_in = date(year, month, day)
print(date_in)

curr_units = float(input("The amount of current remaining units: "))
print("THE DATE UNITS ARE CALCULATED")
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

curr_date = date(year, month, day)
print(curr_date)
print('*'*50)

units_diff = total_units - curr_units
date_diff = curr_date - date_in
print("Number of days used", date_diff.days, "days")
print("\n")
print("Consider the below;")
units_per_week = format(units_diff/(date_diff.days/7), '.5f')
units_per_day = format(units_diff/date_diff.days, '.5f')
units_per_hour = format(units_diff/(date_diff.days*24), '.5f')
units_per_minute = format(units_diff/(date_diff.days*1440), '.5f')
units_per_second = format(units_diff/(date_diff.days*86400), '.5f')

print("\nPer week aprroximatel", units_per_week, "units(kwh) are used")
print("per day", units_per_day)
print("per hour", units_per_hour)
print("per minute", units_per_minute)
print("per second", units_per_second)





