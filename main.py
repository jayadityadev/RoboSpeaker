import pyttsx3


def tts_engine(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def welcome():
    welcome_string = '\nWelcome to RoboSpeaker 1.0. Created by Jayaditya Dev.'
    print(welcome_string)
    tts_engine(welcome_string)
    print("[Type 'qq' to exit.]\n")


if __name__ == '__main__':
    welcome()
    while True:
        text = input("Enter what you want to say: ")
        if text == 'qq':
            tts_engine("Thank you for using me, see you later.")
            print("Thank you for using me, see you later.")
            break
        tts_engine(text)
