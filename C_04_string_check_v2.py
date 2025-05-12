# Functions go here
def string_check(question: object, valid_ans_list: object, num_letters: object) -> object:
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses
    :rtype: object"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_film = string_check("Do you like film? ",
                         yes_no_list, num_letters = 1)
print(f"You chose {like_film}")
pay_method = string_check("payment method: ", payment_list, num_letters = 2)
print(f"You chose {pay_method}")
