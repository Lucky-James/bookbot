def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    letter_count = []
    for letters in num_letters:
        count = num_letters[letters]
        newdict = {"letter": letters, "count": count }
        letter_count.append(newdict)
    letter_count.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/Frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for i in range(0, len(letter_count)):
        if letter_count[i]['letter'].isalpha() == True:
            print(f"The {letter_count[i]["letter"]} character was found {letter_count[i]["count"]} times")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letter_count = {}
    for c in text:
        lower_text = c.lower()
        if lower_text in letter_count:
            letter_count[lower_text] += 1
        else:
            letter_count[lower_text] = 1
    return letter_count

def sort_on(dict):
    return dict["count"]


main()
