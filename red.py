def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found!")
        return

    # a. Total number of characters, words, lines
    total_chars = sum(len(line) for line in lines)
    total_words = sum(len(line.split()) for line in lines)
    total_lines = len(lines)

    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Total lines: {total_lines}")

    # b. Frequency of each character
    char_freq = {}
    for line in lines:
        for ch in line:
            char_freq[ch] = char_freq.get(ch, 0) + 1

    print("\nCharacter frequencies:")
    for ch, freq in sorted(char_freq.items()):
        if ch == '\n':
            display = "\\n"
        elif ch == '\t':
            display = "\\t"
        else:
            display = ch
        print(f"'{display}': {freq}")

    # c. Print words in reverse order
    words = []
    for line in lines:
        words.extend(line.split())
    print("\nWords in reverse order:")
    print(' '.join(words[::-1]))

    # d. Copy even lines to File1, odd lines to File2 (1-based lines)
    with open('File1.txt', 'w') as f1, open('File2.txt', 'w') as f2:
        for idx, line in enumerate(lines, start=1):
            if idx % 2 == 0:
                f1.write(line)
            else:
                f2.write(line)

    print("\nCopied even lines to 'File1.txt' and odd lines to 'File2.txt'.")

# Example usage:
filename = input("Enter filename: ")
process_file(filename)
