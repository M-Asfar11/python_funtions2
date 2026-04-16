# average of 3 numbers 

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(1,2,3)


# built in functions

print("hello", end=" ") # sep = " "
print("asfar") # end = "\n"

# len()

# range()


# calculate product of number 

def cal_prod(a=1, b=1):
    print(a*b)
    return a * b

cal_prod()

# function to print len of cities in list
cities = ["fsd", "lahore", "multan", "karachi", "isb", "grw"]

heroes = ["thor", "ironman", "captian", "howkaye"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

# print the elements of a list in a sinle line

def print_ele(list):
    for item in list: 
        print(item, end=" ")

print_ele(cities)
print_ele(heroes)
print()


# program to find the factorial of n 

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


cal_fact(5)


# function to convert usd to pkr 

def converter(usd_val):
    pkr_value = usd_val * 278
    print(usd_val, "USD =", pkr_value, "PKR")

converter(166)

def even_odd(val):
    if(val % 2 == 0):
        print("Even")
    else:
        print("ODD")

even_odd(9)