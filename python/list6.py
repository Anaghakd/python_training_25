list1 = [int(element) for element in input('Enter the integers separated by @: ').split('@')]

print(list1)

#Another code

def my_function(some_list):
    some_list.remove(10)
    some_list.insert(1, 25)
    some_list.append(50)

#some_list is just a reference list not the main list
    
print('Enter space separated numbers')
list2 = list(map(int,input().split()))
print(list2)
my_function(list2)
print(list2) 

 