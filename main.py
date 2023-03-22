# Jose Nodarse

def encode(data):
    final_data = ''
    encoded_data = 0
    runs = len(data)
    for i in range(runs):
        num = int(data[i])
        encoded_data += num + 3
        final_data += str(encoded_data)
        encoded_data = 0

    return final_data


def decode(data):
    pass


def main():
    game_continue = True

    print("Menu")  # prints the menu
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    while game_continue:  # keeps game going until game_continue = False
        user_input = int(input("Please enter an option: "))
        conversion_data = ''

        if user_input == 1:  # obtains user input and sends it to the encode function
            pass_to_encode = input("Please enter your password to encode: ")

            conversion_data = encode(pass_to_encode)

            print("Your password has been encoded and stored!")
        elif user_input == 2:  # takes the stored encoded user input and decodes it back to the original input.
            print(conversion_data)
            pass

        elif user_input == 3:
            game_continue = False
        else:
            game_continue = False


if __name__ == "__main__":
    main()
