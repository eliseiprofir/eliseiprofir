# IMPORTANT: Install this exact package - pip install googletrans==3.1.0a0

from googletrans import Translator


def get_input() -> tuple[str, str]:
    text: str = input("Enter the text you want to translate in what language you need: ")
    lang: str = input("Enter to what language you want to translate ('en', 'fr', 'es', 'ro', etc.): ")
    return text, lang


def main() -> None:
    translator: Translator = Translator()
    print("Hello to Google Translate. :)")
    print()
    text, lang = get_input()
    translation: str = translator.translate(text, dest=lang).text
    print(translation)
    print()


if __name__ == "__main__":
    main()
