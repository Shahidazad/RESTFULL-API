def hello():
    print("Hello!")


hello()



def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")




def print():
    print("Hello, world!")  # Error!



friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]  # Another way of adding to a list!


add_friend()
print(friends) 





def say_hello():
    print("Hello!")
say_hello()




def add_friend():
    friends.append("Rolf")


friends = []
add_friend()

print(friends) 