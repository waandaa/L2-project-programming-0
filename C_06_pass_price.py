# Functions go here
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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
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


# Main Routine goes here

# intialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Pass Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

#loop for testing purposes...
while True:
    print()

    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ", 10, 121)

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child pass price is $7.50
    elif 12 <= age < 16:
        pass_price = CHILD_PRICE

    # Adult pass ($10.50)
    elif 16 <= age < 65:
        pass_price = ADULT_PRICE

    # Senior Citizen pass ($6.50)
    elif 65 <= age < 121:
        pass_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = pass_price * CREDIT_SURCHARGE

    # calculate total payable...
    total_to_pay = pass_price + surcharge

    print(f"{name}'s pass cost ${pass_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")


