
# Python Dates

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()

print(x) # 2024-04-26 12:15:56.643021


print(x.year) # 2024


# strftime() Method

print(x.strftime("%A")) # Friday

print(x.strftime("%B")) # April

print(x.strftime("%c")) # Fri Apr 26 12:15:56 2024

print(x.strftime("%x")) # 04/26/24

print(x.strftime("%X")) # 12:15:56

print(x.strftime("%Z")) # UTC

print(x.strftime("%c")) # Fri Apr 26 12:15:56 2024



#? Creating Date Objects

# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# Example

#? Create a date object:

import datetime

y = datetime.datetime(2024, 5, 17)

print(y) # 2024-05-17 00:00:00