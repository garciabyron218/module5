# Byron Garcia
# 2/25/24
# program that will go through 1-50 and will print the number, if its divisible by 3, 5 or both, it will let us know
#
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)