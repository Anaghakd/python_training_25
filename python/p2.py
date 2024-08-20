#Read a number from the user and check if it's an even or not

#To read data frpm console we can use input(). However the input() always reads a string s usual with other languages .
#We must first cast a string into a no. [specifically an int()]

#The input(), not only reads a string but also can print a string


my_number =int(inout('Enter a number to check if it is Even or not:'))
print(type(my_number))
if  my_number % 2==0:
    print(my_number, 'is an even number')
else:
    print(my_number, ' is not an even number')
    