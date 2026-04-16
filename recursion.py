def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))

# recursive function to calculate the sum of first n natural numbers 

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(4)
print(sum)


# recursive  function to print all elements in a list. 

def print_list(list, idx=0):
    if (idx == len(list)):
        return  
    print(list[idx])
    print_list(list, idx + 1)

cities = ["fsd", "lahore", "multan", "karachi", "isb", "grw"]

print_list(cities)