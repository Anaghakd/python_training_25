#Program to find count of digits of a number

num=int(input('Enter the number whose sum of digits is to be found: '))
t = num
count = 0
while num != 0:
    j = num % 10
    count += 1
    num = num // 10
print(count, ' is the sum of digit in ', t) 