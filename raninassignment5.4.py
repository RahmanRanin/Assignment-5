while True:
    input_str = input("Enter a string (or 'done' to exit): ")

    if input_str.lower() == 'done':
        break

    special_characters = [',', '.', ':', '!', '?']
    for char in special_characters:
        input_str = input_str.replace(char, '')

    input_str = input_str.upper()

    print(input_str)
