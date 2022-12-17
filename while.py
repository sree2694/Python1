
number = 1

while number <= 100:
    print(number)
    number += 1

number = 1

# while True:
#     print(number)
#     number += 1

number = 1

while True:
    print(number)
    if number == 100:
        break
    number += 1

number = 1

while True:
    number += 1
    if number == 100:
        break
    if number % 2:
        continue
    print(number)