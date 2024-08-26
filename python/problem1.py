#Problem 1
#Count the nummber of perfect squares in thelist of numbers

def count_perfect_squares(numbers):
    perfect_sqaure = 0
    for number in numbers:
        if int(number ** 0.5) ** 2 ==number:
            perfect_sqaure += 1
    return perfect_sqaure
numbers = [1,2,3,4,5,6,7,8,9,10]
result = count_perfect_squares(numbers)
print(f'Number of customers eleigible of discount : {result}')


    