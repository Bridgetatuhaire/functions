#a python program that counts the total number of even and old number in the tuple
#numbers = (1,2,3,4,5,6,7,8)

numbers = (1,2,3,4,5,6,7,8)

# #initializing count for both even and odd numbers
count_even = 0
count_odd = 0
for x in numbers:
    if x % 2 == 0: #checking the number whether it is even
        count_even += 1
    else:
     count_odd += 1
print(f"The even number count is {count_even} and the odd number count is {count_odd}")


#using functions

def count_even_and_odd(data):
    count_even = 0
    count_odd = 0

    for num in data:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print(f"The even number count is {count_even} and the odd number count is {count_odd}")


count_even_and_odd(numbers)

 #create a program that returns the sum multiples of seven and multiples of five
#numbers = [1,7,20,35,49,50]

data = [1, 7, 20, 35, 49, 50]
def sum_of_multiples_seven_and_five(data):
    sum_of_multiples_of_seven = 0
    sum_of_multiples_of_five = 0
    
    for x in data:
        if x % 7 == 0: 
           sum_of_multiples_of_seven += x
        if x % 5 == 0:
            sum_of_multiples_of_five +=x
    print(f'{sum_of_multiples_of_seven}, {sum_of_multiples_of_five}')

sum_of_multiples_seven_and_five(data)










    

