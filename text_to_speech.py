import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("welcome to robo chat, to quite write 'q' alone, and press enter :)")
    
    while True:
        input_text = input("Enter the text you want to convert to speech: ")

        if input_text == "by robo":
            print("Thanks for using robo talk")
            break
        text_to_speech(input_text)