import pyttsx3


if __name__ == '__main__':

    engine = pyttsx3.init()

    welcome_string = '\nWelcome to RoboSpeaker 1.0. Created by JD.'
    print(welcome_string)
    engine.say(welcome_string)
    engine.runAndWait()

    print("[Type 'qq' to exit.]\n")

    while True:
        x = input("Enter what you want to say: ")
        if x == 'qq':
            engine.say("Thank you for using me, see you later.")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
