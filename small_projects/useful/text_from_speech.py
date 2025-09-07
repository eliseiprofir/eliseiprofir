from speech_recognition import Recognizer, AudioFile
import sys


def audio_to_text(recognizer):
    try:
        audio: str = input("Enter the audio file name you want to transcribe (ex. [filename].[extension]): ")
        with AudioFile(audio) as audio_file:
            audio = recognizer.record(audio_file)
        return recognizer.recognize_google(audio)
    except FileNotFoundError:
        print("File not found. Run the program again!")
        sys.exit()


def main():
    recognizer = Recognizer()
    print("Hello to this program who can recognize text from audio file.\n")
    print("Make sure to have the audio file in the same folder with this program.\n")

    text_recognized: str = audio_to_text(recognizer)

    print()
    print("Here is the text:")
    print(text_recognized)
    print()
    input("Thank you for using my program!\n")


if __name__ == "__main__":
    main()
