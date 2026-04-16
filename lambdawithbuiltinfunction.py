numbers = [1,2,3,4,5]

doubled = list(map(lambda x: x *2, numbers))
print(doubled)

nums = [1,2,3,3,3,3]
odd_numbers = list(filter(lambda x : x % 2 != 0, nums))
print(odd_numbers)

students = [("Asfar", 25), ("Musa", 22), ("Ahmad", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)