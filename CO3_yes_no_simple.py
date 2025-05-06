# functions go here...
def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes (y) or no (n).\n")


# Main routine goes here

# loop for testing purposes...
while True:
    want_options = yes_no("Do you want to read the options? ")
    print(f"You chose {want_options}\n")
