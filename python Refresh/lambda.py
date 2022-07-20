def add(x, y):
    return x + y

# Lambdas are just functions without a name.

print(add(5, 7))

# -- Written as a lambda --

add = lambda x, y: x + y
print(add(5, 7))




def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [
    double(x) for x in sequence
]  
doubled = map(double, sequence)
print(list(doubled))

sequence = [1, 3, 5, 9]

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))


# They are used to return a value calculated from its parameters.
