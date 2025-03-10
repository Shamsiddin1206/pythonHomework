import os
import string
from collections import Counter


def create_sample_file():
    text = input("Enter a paragraph to store in 'sample.txt':\n")
    with open("sample.txt", "w") as file:
        file.write(text)


def read_file():
    with open("sample.txt", "r") as file:
        return file.read()


def count_word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()
    return Counter(words)


def write_report(total_words, word_counts):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in word_counts.most_common(5):
            file.write(f"{word} - {count}\n")


def main():
    if not os.path.exists("sample.txt"):
        create_sample_file()

    text = read_file()
    word_counts = count_word_frequency(text)
    total_words = sum(word_counts.values())

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word} - {count} times")

    write_report(total_words, word_counts)
    print("Word count report saved to 'word_count_report.txt'")


if __name__ == "__main__":
    main()
