filename = input("Enter file name: ")

try:
    file = open(filename, 'rt')

    counts = {}

    for line in file:
        for char in line:
            if char.isalpha():
                char = char.lower()

                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1

    file.close()

    for letter in sorted(counts.keys()):
        print(letter, "->", counts[letter])

except FileNotFoundError:
    print("File not found!")