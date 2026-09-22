# Computational Thinking & Coding - Week 3
# Finger Exercises (Lectures 5 & 6)
# Name: Badaila Samir

# ==============================================================================
# LECTURE 5: FLOATS AND APPROXIMATION
# ==============================================================================

# Approximation method for square root (Lecture 5, Slide 26)
'''
x = 36
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
'''

# Fourth root by incremental approximation (Worksheet R03, Exercise 3)
'''
number = 16
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0

while abs(number - (ans**4)) >= epsilon and ans**4 <= number:
    ans += increment
    num_guesses += 1

print('num_guesses =', num_guesses)
print(ans, 'is close to fourth root of', number)
'''


# ==============================================================================
# LECTURE 6: BISECTION SEARCH & FUNCTIONS
# ==============================================================================

# Range checker function (Worksheet R03, Warm-up)
'''
def check_in_range(x, start, end):
    if x >= start and x <= end:
        return "Yes"
    else:
        return "No"

print(check_in_range(3, 1, 5))
print(check_in_range(3, 5, 7))
'''

# Perfect numbers (Worksheet R03, Exercise 2)
'''
def perfect_number(n):
    my_sum = 0
    for x in range(1, n):
        if n % x == 0:
            my_sum += x
    return my_sum == n

print(perfect_number(6))
print(perfect_number(28))
'''

# Fourth root by bisection search (Worksheet R03, Exercise 1)
x = float(input("Using bisection search calculate the forth root of: "))
epsilon = 0.01
low = 0
high = x
ans = (high + low) / 2

while abs(ans**4 - x) >= epsilon:
    if ans**4 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2

print("Forth root of " + str(x) + " is approximately " + str(ans))
