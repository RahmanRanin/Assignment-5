input_str = input("Enter a string: ")
length = len(input_str)

while length > 0:
    print(input_str[length - 1])
    length -= 1
