def capitalize_words(input_string):
    result = input_string.title()
    return result

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    capitalized_string = capitalize_words(user_input)
    print("Capitalized String:", capitalized_string)
