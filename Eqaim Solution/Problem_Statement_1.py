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