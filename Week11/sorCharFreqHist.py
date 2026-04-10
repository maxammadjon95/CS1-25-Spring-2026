filename = input("Enter file name: ")

try:
    with open(filename, 'rt') as file:
        counts = {}

        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    counts[char] = counts.get(char, 0) + 1

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    output_name = filename + ".hist"

    with open(output_name, 'wt') as out:
        for letter, count in sorted_counts:
            out.write(f"{letter} -> {count}\n")

    print("Histogram saved to:", output_name)

except FileNotFoundError:
    print("File not found!")