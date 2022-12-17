# Numbers that are divisible by just 1 and itself are called prime numbers

# Declare a variable to store an integer number
isPrimeNumber = 13
for number in range(2, isPrimeNumber):
    # Check if 'isPrimeNumber' is divisible by any other number in the range 2 to isPrimeNumber - 1
    if isPrimeNumber % number is 0:
        print('Number is not a prime number.')
        break
# If 'isPrimeNumber' was divisible by no other number, the else corresponding to the for loop gets executed
else:
    print('Number is a prime number')

# Output: Number is a prime number
