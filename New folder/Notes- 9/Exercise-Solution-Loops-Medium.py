# Declare a variable to keep track of the sum of odd numbers
oddSum = 0
# Run a for loop from 1 to 10
for number in range(1, 11):
    # Check if the number is odd by checking if it is not divisible by 2
    if number % 2 is not 0:
        oddSum = oddSum + number
print(oddSum)
