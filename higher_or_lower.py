from random import randrange

def user_input():
    user_guess = input("Please enter a number between 0 and 10  ")
    return int(user_guess)

def random_number():
    return randrange(11)

def user_right_or_wrong(num1, num2):
    if num1 > num2:
        print("No, too high!")
    elif num1 < num2:
        print("No! Too low!")
    else:
        print("Yes! You guessed correctly!")
        
guess = user_input()
random = random_number()

user_right_or_wrong(guess, random)

print(f"Your number: {guess}")
print(f"Random number: {random}")