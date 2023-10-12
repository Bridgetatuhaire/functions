#write a python function that finds a maximum of 3 numbers
def maximum_of_three_numbers(a, b, c):
    if a>b and c:
        print(f"{a} is greater than {b} and {c}")
    elif b>a and c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

maximum_of_three_numbers(70,80,90)
maximum_of_three_numbers(99,79,65)

#Write a Python function to sum all the numbers in a list.

def sum_numbers_in_list(numbers):
    total = 0
    for x in numbers:
        total += x
        return total
    print(sum[8,2,3,0,7])
