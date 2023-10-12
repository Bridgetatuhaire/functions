#1.python programme to reverse a string [1,2,3,4,a,b,c,d]
def string_reverse(str1):

    rstr1 = ''   # creating an empty string to store the reversed string
    index = len(str1)    #calculating the lenght of a string
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1,2,3,4,a,b,c,d'))

#A python proramme to print the even numbers from a given list
    # {1,2,3,4,5,6,7,8,9}
def even_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)

# Define the input list
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call the function and pass the list as an argument
even_numbers(numbers_list)