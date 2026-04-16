# def double(x):
#     return x * 2

double = lambda x: x*2
cube = lambda x: x*x*X
    
print(double(4))


# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

avg = lambda x,y: (x+y) / 2
avg = lambda x,y,z: (x + y + z) / 3

# print(avg(3,4))
print (avg(3, 4, 10))

def appl(fx, value):
    return 6 + fx(value)

print(appl(cube, 2))
