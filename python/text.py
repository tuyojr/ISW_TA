from tkinter import *
import tkinter.messagebox
from translate import Translator
import speech_recognition as sr
import pyttsx3

Screen = Tk()
Screen.title("Language Translator")
Screen.geometry("500x350")
Screen.configure(bg="white smoke")

speech_recognizer = sr.Recognizer()

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

Input_lang = StringVar()
Output_lang = StringVar()
Languages = {'Hindi', 'German', 'English', 'French', 'Spanish', 'Japanese', 'Chinese', 'Russian', 'Italian', 'Korean', 'Arabic', 'Hindi'}

Input_lang.set('English')
Output_lang.set('French')

# if the user clicsk the text button, the text input will be 
# enabled and the speech input will be disabled
def text_input_button_click():
    text_input.config(state=NORMAL)
    speech_input_button.config(state=DISABLED)
    # show a messagebox to tell the user to input the text
    tkinter.messagebox.showinfo("Text Input", "Please input the text")

def speech_input_button_click():
    text_input_button.config(state=DISABLED)
    speech_input_button.config(state=NORMAL)
    tkinter.messagebox.showinfo("Speech Input", "Please allow the microphone to record your voice")
    try:
        with sr.Microphone() as source:
            speech_recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = speech_recognizer.listen(source)
            text_input.config(state=NORMAL)
            text_input.delete(0, END)
            text_input.insert(0, speech_recognizer.recognize_google(audio))
            text_input.config(state=DISABLED)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")

text_input_button = Button(Screen, text="Text", font="arial 7", bg="white smoke", command=text_input_button_click)
text_input_button.place(x=100, y=10)

speech_input_button = Button(Screen, text="Speak", font="arial 7", bg="white smoke", command=speech_input_button_click)
speech_input_button.place(x=300, y=10)

TextVar = StringVar()
text_input = Entry(Screen, width=70, font="arial 7", bg="white smoke", textvariable=TextVar)
text_label = Label(Screen, text="Text Input", font="arial 7", bg="white smoke")
text_label.place(x=20, y=100)
text_input.place(x=80, y=100)

OutputVar = StringVar()
translation_output = Entry(Screen, width=70, font="arial 7", bg="white smoke", textvariable=OutputVar)
translation_label = Label(Screen, text="Translation Output", font="arial 7", bg="white smoke")
translation_label.place(x=20, y=150)
translation_output.place(x=110, y=150)

Input_lang_button = OptionMenu(Screen, Input_lang, *Languages)
Input_lang_button.place(x=30, y=50)
Output_lang_button = OptionMenu(Screen, Output_lang, *Languages)
Output_lang_button.place(x=300, y=50)

def Translate():
    translator = Translator(from_lang = Input_lang.get(), to_lang = Output_lang.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)
    # reset the buttons after translating
    text_input.config(state=NORMAL)
    speech_input_button.config(state=NORMAL)
    SpeakText(OutputVar.get())

translate_button = Button(Screen, text="Translate", font="arial 7", bg="white smoke", command=Translate)
translate_button.place(x=210, y=200)

exit_button = Button(Screen, text="Exit", font="arial 7", bg="white smoke", command=Screen.destroy)
exit_button.place(x=220, y=300)



Screen.mainloop()