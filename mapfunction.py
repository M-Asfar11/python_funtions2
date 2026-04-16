# def cube(x):
#     return x * x *x 

# print(cube(2))

l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))
newl = map(lambda x: x*x*x , l)
print(list(newl)) # map function returns you map object not
                        # result you have to convert
                       #  it into your deired type 

# you can write direct lambda function in the high order function 

