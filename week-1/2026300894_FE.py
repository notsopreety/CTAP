# Strings FE
'''
word = "hello"
print(word[0])
print(word[2:4])
print(word + " world!")
print(word * 3)
print(len(word))
'''

# Input and Output FE
'''
name = input("What is your name? ")
age = input("How old are you? ")

print("Hello, " + name + "!")
print("You will be " + str(int(age) + 1) + " years old next year.")
'''

# Branching FE
age = int(input("Enter your age: "))
if age <= 0:
    print("Oh gosh do you really exist?")
elif age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
elif age <= 120:
    print("You are a senior citizen.")
else:
    print("I guess you're immortal.")