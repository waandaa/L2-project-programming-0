# Functions go here

def make_statement(statement, decoration):

    print(f"{decoration * 3} {statement} {decoration * 3}")



def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word
       or the 'n' letter/s of a word from a list of valid responses
       :rtype: object"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("instructions", "❕")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and the profit).

Once you have either sold all of the tickets or entered 
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the
draw (their ticket is free).
    
    ''')

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again")

def int_check(question, low, high):
    """Checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# intialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement("Mini Movie festival", "🍿")

print()

want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
while tickets_sold < MAX_TICKETS:
    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ", 10, 121)

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has bought a pass ({pay_method})")
    print("")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets)s")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
