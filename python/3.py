import pdb
pdb.set_trace()

def find_sum_of_digits(num):
    sum = 0
    while num != 0:
        remainder = num % 10
        num = num // 10
        sum += remainder
    return sum

input_number = int(input('Enter a number to find sum of itsl digits'))

sum_of_digits = find_sum_of_digits(input_number)

print(f'Sum of digitsof {input_number} is {sum_of_digits}')
