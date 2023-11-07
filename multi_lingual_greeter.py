""" 
This function takes a parameter for a name and 
will then print it out
"""


def greet(name):
    print(f"Hello, {name}. Welcome to Zip Code!")


"""
This function will print out the name provided
"""

def name_input():
    return input("Please provide your name: ")


def language_input(name):
    print("English\nSpanish\nFrench")
    choice = input("Please choose a language: ")
    choice = choice.lower()
    if choice == "english":
        print(f"Hello {name}. Welcome")
    elif choice == "spanish":
        print(f"Hola! {name}. Bienvenidos!")
    elif choice == "french":
        print(f"Bonjour {name}. Bienvenue!")
    else:
        print("Sorry, that doesn't exist")



user_name = name_input()

language_input(user_name)


# greet(user_name)

