morse_dict = {}

with open('morse.txt', 'r') as file:
    for line in file:
        key, value = line.split()
        morse_dict[key] = value

# print(morse_dict)
def main():
    user_input = input(f"Enter text here: ")
    translated = []

    for letter in user_input:
        if letter.capitalize() in morse_dict:
            translated.append(morse_dict[letter.capitalize()])
        else:
            translated.append(letter)

    trans_str = ''.join(i for i in translated)
    print(trans_str)

if __name__ == '__main__':
    main()


