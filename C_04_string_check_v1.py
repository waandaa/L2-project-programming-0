# Functions go here
def string_check(question, valid_ans_list):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here
passes = ['cinephiles accreditation', 'three days in Cannes accreditation', 'marche du film accreditation']

like_film = string_check("Do you like film? ", ['yes', 'no'])
print(f"You chose {like_film}")
choose_pass = string_check("choose from one of our passes:", passes)
print(f"You chose {choose_pass}")
