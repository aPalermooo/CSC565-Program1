from share.Message import Message

DIVIDER = '\n' + ('-' * 30) + '\n'

OPTIONS = {"Exit": None,
               "Distance": ("Kilometers", "Miles"),
               "Weight": ("Kilograms", "Pounds"),
               "Temperature": ("Celsius", "Fahrenheit")}

def create_message(connection_type : str) -> Message:
    print(f"Starting Client...\n\t(Connection Type: {connection_type}){DIVIDER}")

    """CONVERSION TYPE"""

    message_type = None #Bring to Scope

    while True: #while user input is invalid

        '''Prompt User'''
        print("Input Number of Desired Conversation:\n")
        for index, (key, value) in enumerate(OPTIONS.items()):
            if index == 0:
                continue
            print(f"{index:}. {key:<16}\t({value[0]:<9}\t <-->\t{value[1]:<11})")
        print(f"0. Quit Program")
        print()


        '''Validate User Input'''
        message_type_input = input("Input:")

        if not message_type_input.isdigit():
            print(f"Input invalid (not a number)"
                  f"\nYou entered: {message_type_input}"
                  f"\nplease try again...{DIVIDER}")
            continue

        message_type = int(message_type_input)

        if message_type  not in range(len(OPTIONS)):
            print(f"Input invalid (not in range)"
                  f"\nYou entered: {message_type}"
                  f"\nplease try again...{DIVIDER}")
            continue

        if message_type == 0:   #User Exit
            print("\nTerminating...\n")
            exit(0)

        break #User input validated

    print(DIVIDER)


    """CONVERSION DIRECTION"""

    options_list = list(OPTIONS.values())
    options_list = options_list[message_type]

    is_metric = None #Bring to scope

    while True: #while user input invalid

        '''Prompt User'''
        print("Input Number of Desired Conversion:\n")
        print(f"1. {options_list[0]} <--> {options_list[1]}")
        print(f"2. {options_list[1]} <--> {options_list[0]}")
        print(f"0. Quit Program\n")

        is_metric_input = input("Input: ")

        '''Validate User Input'''
        if not is_metric_input.isdigit():
            print(f"Input invalid (not a number)"
                  f"\nYou entered: {message_type_input}"
                  f"\nplease try again...{DIVIDER}")
            continue

        if is_metric_input not in ("1","2","3"):
            print(f"Input invalid (not in range)"
                  f"\nYou entered: {message_type}"
                  f"\nplease try again...{DIVIDER}")
            continue

        match is_metric_input:
            case "0":
                print("\nTerminating...\n")
                exit(0)
            case "1":
                is_metric = True
            case "2":
                is_metric = False

        print(is_metric)
        break





def return_message(message : Message):
    print("Hello World")


def main():
    message = create_message("TEST")
    return_message(message)

if __name__ == "__main__":
    main()

