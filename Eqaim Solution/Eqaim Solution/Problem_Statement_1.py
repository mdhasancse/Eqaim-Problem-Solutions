# Problem Statement 1: Write a script in python or javascript to find the solution of the following problem
# How many two or more digit numbers can you make such that digits on left are always smaller than the digits on the right in the number?

# For e.g.

# 189 is valid (because 1<8<9 and it is at least two digit number)
# 198 is not valid
# 288 is n


def is_valid_number(n):
    digits = [int(j) for j in str(n)]
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            return False
    return True

is_count = 0

for i in range(10, 100):
    if is_valid_number(i):
        is_count += 1

for i in range(100, 1000):
    if is_valid_number(i):
        is_count += 1

print(is_count)


number = 189
if is_valid_number(number):
    print(number," is valid")
else:
    print(number, " is not valid")