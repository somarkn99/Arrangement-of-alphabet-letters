def get_letters(numbers):
    letters = []
    for number in numbers:
        if 1 <= number <= 26:
            letter = chr(ord('A') + number - 1)
            letters.append(letter)
        else:
            letters.append("Invalid input")
    return letters

numbers = input("Enter the numbers of the letters (1-26) separated by spaces: ").split()
numbers = [int(number) for number in numbers]
letters = get_letters(numbers)
print("The letters are:", " ".join(letters))