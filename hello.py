import random
from datetime import datetime
import csv

def generate_random_number():
    return random.randint(1, 100)

def get_current_time():
    return datetime.now()

def get_sum_result():
    import random

    # Generate two random numbers between 1 and 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Calculate the sum of the two numbers
    sum_result = num1 + num2

    # Print the numbers and the sum
    print("Number 1:", num1)
    print("Number 2:", num2)
    
    return sum_result

def main():
    random_number = generate_random_number()
    print(f"Random Number: {random_number}")

    current_time = get_current_time()
    print(f"Current Time: {current_time}")

    sum_result = get_sum_result()
    print(f"Sum is: {sum_result}")

    csv_file = 'airline-passengers.csv'  
    output_file = 'output.txt' 

    # Read the CSV file and extract all values
    values = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row:  # Skip empty rows
                values.extend(row)

    # Save the CSV content to a text file
    with open(output_file, 'w') as file:
        for row in values:
            file.write(','.join(row) + '\n')


if __name__ == '__main__':
    main()





