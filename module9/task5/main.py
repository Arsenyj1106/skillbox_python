import os
os.chdir('C:\Users\pirog\OneDrive\Рабочий стол\module9\task5')

with open("text.txt", "r") as file:
    text = file.read()

letter_frequencies = {}

for char in text:
    if char.isalpha() and char.isascii():
        char = char.lower()
        if char in letter_frequencies:
            letter_frequencies[char] += 1
        else:
            letter_frequencies[char] = 1

total_letters = sum(letter_frequencies.values())

sorted_letters = sorted(letter_frequencies.items(), key=lambda x: (-x[1], x[0]))

with open("analysis.txt", "w") as output_file:
    for letter, frequency in sorted_letters:
        letter_percentage = (frequency / total_letters)
        output_file.write(f"{letter} {letter_percentage:.3f}\n")