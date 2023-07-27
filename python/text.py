from tkinter import *
import tkinter.messagebox
from translate import Translator
import speech_recognition as sr
import pyttsx3
import cv2
import pytesseract

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
    tkinter.messagebox.showinfo("Text Input", "Please input the text.")

def speech_input_button_click():
    text_input_button.config(state=DISABLED)
    speech_input_button.config(state=NORMAL)
    tkinter.messagebox.showinfo("Speech Input", "Please allow the microphone to record your voice.")
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

def image_input_button_click():
    text_input_button.config(state=DISABLED)
    speech_input_button.config(state=DISABLED)
    image_input_button.config(state=NORMAL)
    tkinter.messagebox.showinfo("Image Input", "Please wait for the camera to come up and scan your text.")
    # Path to the Tesseract OCR executable (Change this if necessary)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Initialize the webcam capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Preprocess the frame (you can add more preprocessing steps here)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform OCR on the preprocessed frame
        extracted_text = pytesseract.image_to_string(gray_frame)

        # Find bounding boxes for the detected characters
        boxes = pytesseract.image_to_boxes(gray_frame)
        for b in boxes.splitlines():
            b = b.split(' ')
            char, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(frame, (x, y), (w, h), ( 255,0, 0), 1)
            cv2.putText(frame, char, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Display the extracted text
        # text_input.delete(0, END)
        text_input.insert(0, extracted_text)

        # Display the original frame with bounding boxes and text
        cv2.imshow('Webcam', frame)

        # Stop the loop when the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

    
text_input_button = Button(Screen, text="Text", font="arial 7", bg="white smoke", command=text_input_button_click)
text_input_button.place(x=100, y=10)

image_input_button = Button(Screen, text="Image", font="arial 7", bg="white smoke", command=image_input_button_click)
image_input_button.place(x=200, y=10)

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
    image_input_button.config(state=NORMAL)
    text_input.config(state=NORMAL)
    speech_input_button.config(state=NORMAL)
    SpeakText(OutputVar.get())

translate_button = Button(Screen, text="Translate", font="arial 7", bg="white smoke", command=Translate)
translate_button.place(x=210, y=200)

exit_button = Button(Screen, text="Exit", font="arial 7", bg="white smoke", command=Screen.destroy)
exit_button.place(x=220, y=300)



Screen.mainloop()