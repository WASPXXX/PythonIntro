# just like argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# another
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# no argument
def print_none():
    print("I got nothin'.")


print_two("Jaden", "Wang")
print_two_again("Jaden", "Wang")
print_one("First!")
print_none()