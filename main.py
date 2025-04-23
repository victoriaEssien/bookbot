import sys
from stats import word_count, get_char_count, sort_char_counts

if (len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
else:
    print("============ BOOKBOT ============")
    print(f"Analyzing book {sys.argv[1]}...")

    word_count()

    char_counts = get_char_count()
    sorted_chars = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['count']}")

    print("============= END ===============")
