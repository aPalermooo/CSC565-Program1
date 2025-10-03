from share.Message import Message

DIVIDER = '\n' + ('-' * 30) + '\n'

OPTIONS = {"Exit": None,
               "Distance": ("Kilometers", "Miles"),
               "Weight": ("Kilograms", "Pounds"),
               "Temperature": ("Celsius", "Fahrenheit")}

def create_message(connection_type : str) -> Message:
    """
    Prompts user for all information required by server API

    :param connection_type: Text string that indicates function of program
    :return: Message Object containing user inputs
    """

    def prompt_type() -> int:

        user_input = 0 #set in scope outside loop

        while True:  # while user input is invalid

            '''Prompt User'''
            print("Input Number of Desired Conversation:\n")
            for index, (key, value) in enumerate(OPTIONS.items()):
                if index == 0:
                    continue
                print(f"{index:}. {key:<16}\t({value[0]:<9}\t <-->\t{value[1]:<11})")
            print(f"0. Quit Program")
            print()

            '''Validate User Input'''
            user_input_dirty = input("Input:")

            if not user_input_dirty.isdigit() or user_input_dirty == "":
                print(f"Input invalid (not a number)"
                      f"\nYou entered: {user_input_dirty}"
                      f"\nplease try again...{DIVIDER}")
                continue

            user_input = int(user_input_dirty)

            if user_input not in range(len(OPTIONS)):
                print(f"Input invalid (not in range)"
                      f"\nYou entered: {message_type}"
                      f"\nplease try again...{DIVIDER}")
                continue

            break #Input valid
        return user_input

    def prompt_direction(m_type : int) -> bool:
        options_list = list(OPTIONS.values())
        options_list = options_list[m_type]

        user_input = False  # Bring to scope

        while True:  # while user input invalid

            '''Prompt User'''
            print("Input Number of Desired Conversion:\n")
            print(f"1. {options_list[0]} <--> {options_list[1]}")
            print(f"2. {options_list[1]} <--> {options_list[0]}")
            print(f"0. Quit Program\n")

            user_input_dirty = input("Input: ")

            '''Validate User Input'''
            if not user_input_dirty.isdigit():
                print(f"Input invalid (not a number)"
                      f"\nYou entered: {user_input_dirty}"
                      f"\nplease try again...{DIVIDER}")
                continue

            match user_input_dirty:
                case "0":
                    print("\nTerminating...\n")
                    exit(0)
                case "1":
                    user_input = True
                    break
                case "2":
                    user_input = False
                    break
                case _: #Default:
                    print(f"Input invalid (not in range)"
                          f"\nYou entered: {user_input_dirty}"
                          f"\nplease try again...{DIVIDER}")
                    continue
        return user_input

    print(f"Starting Client...\n\t(Connection Type: {connection_type}){DIVIDER}")

    """CONVERSION TYPE"""

    message_type = prompt_type()
    print(DIVIDER)

    """CONVERSION DIRECTION"""

    is_metric = prompt_direction(message_type)
    print(DIVIDER)





    #TODO Prompt User for Value
        #Check if is negative !! (if not temp)

    #TODO: Return message to caller





def return_message(message : Message):
    print("Hello World")


def main():
    message = create_message("TEST")
    return_message(message)

if __name__ == "__main__":
    main()

