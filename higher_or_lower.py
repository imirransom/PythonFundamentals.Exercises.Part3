from random import randrange

def user_input():
    user_guess = input("Please enter a number between 0 -and 10  ")
    return int(user_guess)

def random_number():
    return randrange(11)

def user_right_or_wrong(num1, num2):
    if num1 == num2:
        print("Yes! You guessed the right number.")
    else:
        print("No! You guessed the wrong number.")

print(f"Your number: {user_input()}")
print(f"Random number: {random_number()}")
user_right_or_wrong(user_input, random_number)