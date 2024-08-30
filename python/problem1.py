#Problem 1
#Count the nummber of perfect squares in thelist of numbers

def count_perfect_squares(numbers):
    perfect_sqaure = 0
    for number in numbers:
        if int(number ** 0.5) ** 2 ==number:
            perfect_sqaure += 1
    return perfect_sqaure
numbers = []
numbers= int(input('Enter the number of bills'))
result = count_perfect_squares(numbers)
print(f'Number of customers eligible of discount : {result}')


    