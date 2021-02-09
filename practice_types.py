# Switching Types
num = 42
pi = 3.142
num = 42/pi
print(num)

number = 42
number = int(42/pi)
print(number)

# LISTS
seasons = ['Winter', 'Spring','Summer', 'Autumn']
print(seasons)
print(seasons[2])
seasons[-1] = 'July'
print(seasons)
# The lines 13 and 14 show to us that the contents of a list can be changed
# By using an index of -1, we are ensuring this list is accessed from right to left
print(seasons[-2])
print(seasons[-4])
print(seasons[0])
# -4 from R to L is the same as 0 from L to R
weekdays = ['Monday', 'Tuesday', 3, 4, 'Friday']
print(weekdays)
print(weekdays[2])

# Multi-dimensional lists seen below
salads = ["chicken", ["halloumi", "cheddar", "blue cheese"], "smoked salmon"]
print(salads)
print(salads[1][1])
print(salads[-2][-2])
salads[1][2] = "Mozarella"
print(salads)

# TUPLES
