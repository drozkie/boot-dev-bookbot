selected_book = "books/frankenstein.txt"

def build_book_report(open_book):
    split_title = selected_book.split('/')
    title = split_title[1].split('.')[0].title()

    print(f"--- Begin report of {title} ---")
    print(f"{count_words(open_book)} words found in this document.\n")

    for letter, count in count_characters(open_book).items():
        print(f"The '{letter}' character was found {count} times")

    print(f"--- End reports ---")

def count_characters(open_book):
    characters = {}

    for character in open_book:
        lower = character.lower()
        if not lower.isalpha():
            continue
        elif lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters

def count_words(book):
    count = book.split()
    return len(count)

def main():
    with open(selected_book) as f:
        open_book = f.read()
        build_book_report(open_book)

main()