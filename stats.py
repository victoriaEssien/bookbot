import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def word_count():
    book_content = get_book_text(sys.argv[1])
    words = book_content.split()
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")


def get_char_count():
    book_content = get_book_text(sys.argv[1])
    characters = book_content.lower()
    char_counts = {}

    for char in characters:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_char_counts(char_counts):
    filtered_counts = [
        {"char": char, "count": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    filtered_counts.sort(key=lambda x: x["count"], reverse=True)
    return filtered_counts
