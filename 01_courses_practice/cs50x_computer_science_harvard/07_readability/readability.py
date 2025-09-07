def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif 1 < index < 17:
        print(f"Grade {index}")
    elif index > 16:
        print(f"Grade 16+")


def count_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i].isalpha():
            count += 1
    return count


def count_words(text):
    count = 1
    for i in range(len(text)):
        if text[i].isspace():
            count += 1
    return count


def count_sentences(text):
    count = 0
    for i in range(len(text)):
        if text[i] in [".", "!", "?"]:
            count += 1
    return count


if __name__ == "__main__":
    main()
