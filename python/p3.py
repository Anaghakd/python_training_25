'''
Accept a number as input, say X and define a logic to get the output say Y. The Input can be only 0 or 1 and the output must be 1 if input is 0 or viceversa.
Do not use Boolean Algebra
'''

X= int(input('Enter the input number(0 or 1 only):'))

#Check if the i/p is valid

Y=1-X
print(f'Input number = {X}, Output number = {Y}')

if X==0:
    y=1
elif X==1:
    Y=0
    