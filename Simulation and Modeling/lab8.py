# Lab Topic: Mid-Square Method of Random Number Generation
# This program generates pseudo-random numbers using the mid-square technique.


def mid_square_method(seed, n_digits, count):
    current_number = seed
    for i in range(count):
        squared_number = current_number ** 2  # Square the number
        squared_str = str(squared_number).zfill(2 * n_digits)  # Ensure at least 2n digits
        mid_index = len(squared_str) // 2  # Find the middle
        new_number = int(squared_str[mid_index - n_digits // 2 : mid_index + n_digits // 2])  # Extract n middle digits
        print(f"X{i} = {new_number}")  # Print generated number
        current_number = new_number  # Update for next iteration

# Input seed value, number of digits, and count of numbers to generate
seed = int(input("Enter the seed value (n-digit number): "))
n_digits = len(str(seed))  # Number of digits in the seed
count = int(input("Enter how many random numbers you want to generate: "))
print("Random Numbers Generated [Bibek Singh]:")  # Print name

# Run the Mid Square Method
mid_square_method(seed, n_digits, count)