import os
import string
from collections import Counter


def create_sample_file():
    if not os.path.exists("sample.txt"):
        print("File 'sample.txt' not found. Please enter some text to create it.")
        with open("sample.txt", "w", encoding="utf-8") as f:
            f.write(input("Enter your text: ") + "\n")


def read_file():
    word_counts = Counter()
    total_words = 0

    with open("sample.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower().translate(str.maketrans("", "", string.punctuation))
            words = line.split()
            word_counts.update(words)
            total_words += len(words)

    return word_counts, total_words


def save_report(total_words, common_words):
    with open("word_count_report.txt", "w", encoding="utf-8") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total_words}\n")
        f.write("Top Words:\n")
        for word, count in common_words:
            f.write(f"{word} - {count}\n")


def main():
    create_sample_file()
    word_counts, total_words = read_file()

    try:
        top_n = int(input("Enter the number of top common words to display: "))
    except ValueError:
        print("Invalid input. Showing top 5 words by default.")
        top_n = 5

    common_words = word_counts.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")

    save_report(total_words, common_words)
    print("\nReport saved to 'word_count_report.txt'.")


if __name__ == "__main__":
    main()
