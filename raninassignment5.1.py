while True:
    input_str = input("Enter two words separated by a space (or 'done' to exit): ")
    
    if input_str == 'done' or not input_str:
        break

    words = input_str.split()
    
    if len(words) == 2:
        word1, word2 = words
        result = min(word1, word2)
        print(f"The word that comes before in lexicographical order is: {result}")
    elif len(words) == 1:
        print("Only one word entered. Please enter two words.")
    else:
        print("Invalid input. Please enter two words separated by a space.")
