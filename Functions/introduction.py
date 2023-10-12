#functions without parameters

def my_course_unit(): #def is a keyword
    print("Programming in Python")
  

def my_name():
    print("Shammirah") #this will not give an output

#calling a function
my_course_unit()
my_name()

#using functions to perform a particular task
#create a function that multiplies two numbers a and b where a=3 and b=10

def product_of_two_numbers(a,b):
    output = a*b
    print(output)

    print(f"The product of {a} and {b} is {output}")

product_of_two_numbers(3,10)




#create a function that returns your name and your age
def my_name_and_age(name, age):
    print(f"My name is {name} and I am {age} years old.")


my_name_and_age("Bridget", 25)

