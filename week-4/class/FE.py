def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False
my_func = is_even
print(my_func(10))  # True