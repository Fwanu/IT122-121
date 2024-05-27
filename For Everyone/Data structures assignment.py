# Function to calculate the average
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Ask for five inputs
inputs = []
for i in range(5):
    number = float(input("Enter number {}: ".format(i+1)))
    inputs.append(number)

# Calculate and print the average
average = calculate_average(inputs)
print("The average of the numbers is:", average)
    