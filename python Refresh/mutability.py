a = []
b = a



a.append(35)  # Modify the value.

print(a)
print(b)


a = []
b = []

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))  # Different from id(a)



# For example integers don't have any such methods, so they are called _immutable_.

a = 8597
b = 8597

print(id(a))
print(id(b))  # Same one

a = 8598

print(id(a))
print(
    id(b)
)  # Different, because we didn't change 8597. We just used the name 'a' for a different value. 'b' still is a name for 8597.


a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

# This means that a becomes a new string containing "helloworld", but b still is a name for "hello".

print(id(a))
print(id(b))