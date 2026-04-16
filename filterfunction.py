# Filter 

l = [1, 2, 4, 6, 4, 3]

def filter_function(a):
    return a > 4


newl = filter(filter_function, l)

print(list(newl))