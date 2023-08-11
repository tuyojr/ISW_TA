from tkinter import *
import tkinter.messagebox
from translate import Translator
import speech_recognition as sr
import pygame
from gtts import gTTS
from io import BytesIO
import cv2
import pytesseract
from PIL import Image, ImageTk

def animate_labels():
    for index, label_info in enumerate(labels):
        canvas.move(animated_labels[index], label_info["speed"], 0)  # Move label
        label_info["x"] += label_info["speed"]

        if label_info["speed"] > 0 and label_info["x"] >= splash.winfo_screenwidth() // 2:
            label_info["speed"] = 0  # Stop the label when it reaches the center
            splash.after(1000, start_main_window)  # Call the function to start the main window

    splash.after(50, animate_labels)  # Schedule the next animation frame

def start_main_window():
    splash.destroy()
    main_window()

def main_window():
    Screen = Tk()
    Screen.title("Quantum Translator")
    # Screen.geometry("1280x700")
    window_width = 1280  # Set your desired width
    window_x = (Screen.winfo_screenwidth() - window_width)

    # Set the position for the main application window
    Screen.geometry(f"{window_width}x700+{window_x}+0")
    # attributes("-fullscreen", True)
    Screen.configure(bg="#D6D5D6")

    speech_recognizer = sr.Recognizer()

    def play_audio(text, lang):
        translated_text = text
        if lang != "English":
            translator = Translator(from_lang="en", to_lang=lang)
            translated_text = translator.translate(text)
        tts = gTTS(text=translated_text, lang=Languages[lang])
        fp_io = BytesIO()
        tts.write_to_fp(fp_io)
        fp_io.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(fp_io)
        pygame.mixer.music.play()
    
    Input_lang = StringVar()
    Output_lang = StringVar()
    # a dictionary of languages and their codes
    Languages = {
        'German': 'de',
        'English': 'en', 
        'French': 'fr', 
        'Spanish': 'es', 
        'Japanese': 'ja', 
        'Chinese': 'zh-CN', 
        'Russian': 'ru',
        'Italian': 'it', 
        'Korean': 'ko', 
        'Arabic': 'ar',
        'Hindi': 'en'
    }
    
    Input_lang.set('English')
    Output_lang.set('French')


    # if the user clicks the text button, the text input will be 
    # enabled and the speech input will be disabled
    def text_input_button_click():
        # show a messagebox to tell the user to input the text
        tkinter.messagebox.showinfo("Text Input", "Please input the text.")
    
    def speech_input_button_click():
        tkinter.messagebox.showinfo("Speech Input", "Please allow the microphone to record your voice.")
        try:
            with sr.Microphone() as source:
                speech_recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = speech_recognizer.listen(source)
                text_input.delete(0, END)
                text_input.insert(0, speech_recognizer.recognize_google(audio))
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")
    
    def image_input_button_click():
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
            # Load your image
            boxes = pytesseract.image_to_boxes(gray_frame)

            for b in boxes.splitlines():
                b = b.split(' ')
                char, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
            text_input.insert(0, extracted_text)

            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 1)

            # Add the accumulated detected text to the image
            cv2.putText(frame, extracted_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Detected Text', frame)

            if cv2.waitKey(0) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()

    def clear_text():
        TextVar.set("")
        translation_output.delete(0, END)

    def exit_program():
        exit = tkinter.messagebox.askyesno("Exit", "Do you want to exit?")
        if exit > 0:
            Screen.destroy()
            return
        

    #################   THREE TOP MOST BUTTON SECTION #################################
    # Calculate the width and height of each button based on the screen width and number of buttons
    num_buttons = 3
    font_nd_size = "arial 24"
    padding = 20  # Adjust this value for the desired padding
    space_between_buttons = 10  # Adjust this value for the desired space
    button_height = 50  # Adjust this value for the desired button height
    available_width = Screen.winfo_screenwidth() - 2 * padding - (num_buttons - 1) * space_between_buttons
    button_width = available_width // num_buttons

    text_input_button = Button(Screen, text="Text", font=font_nd_size, bg="white", fg="black", command=text_input_button_click, borderwidth=2, relief="ridge")
    text_input_button.place(x=padding, y=10, width=button_width, height=button_height, bordermode=OUTSIDE)

    image_input_button = Button(Screen, text="Image", font=font_nd_size, bg="white",  fg="black", command=image_input_button_click, borderwidth=2, relief="ridge")
    image_input_button.place(x=padding + button_width + space_between_buttons, y=10, width=button_width, height=button_height, bordermode=OUTSIDE)

    speech_input_button = Button(Screen, text="Speak", font=font_nd_size, bg="white", fg="black", command=speech_input_button_click, borderwidth=2, relief="ridge")
    speech_input_button.place(x=padding + 2 * (button_width + space_between_buttons), y=10, width=button_width, height=button_height, bordermode=OUTSIDE)


    TextVar = StringVar()
    OutputVar = StringVar()

    ##################     TEXT INPUT AND TRANSLATOR OUTPUT ENTRY FIELD & LABEL SECTION   ###############
    # Calculate the width and height for the input fields and labels
    field_width = int(Screen.winfo_screenwidth() * 3 / 4) - 40  # 3/4 of the screen width, subtract padding
    field_height_text = 100  # Adjust this value for the desired field height
    field_height_trans = 150 

    # Calculate the x-coordinate to center the input fields and labels
    field_x = (Screen.winfo_screenwidth() - field_width) // 2

    text_label = Label(Screen, text="Text Input", font="arial 18", bg="#D6D5D6", fg="black")
    text_label.place(x=field_x, y=180)

    text_input = Entry(Screen, width=50, font="arial 28", bg="white smoke", textvariable=TextVar)
    text_input.place(x=field_x, y=230, width=field_width, height=field_height_text)

    translation_label = Label(Screen, text="Translation Output", font="arial 18", bg="#D6D5D6", fg="black")
    translation_label.place(x=field_x, y=350)

    translation_output = Entry(Screen, width=50, font="arial 28", bg="white smoke", textvariable=OutputVar)
    translation_output.place(x=field_x, y=400, width=field_width, height=field_height_trans)

    ###################         CHOOSE LANGUAGE BUTTONS  SECTION        ##########################
    # Adjust the button width and height for Input_lang and Output_lang buttons
    button_width_small = 150
    button_height_small = 40
    space_between_buttons = 900  # Adjust this value for the desired space

    # Calculate the total width required for both buttons and the space
    total_width = 2 * button_width_small + space_between_buttons

    # Calculate the x-coordinate to center the buttons and space
    button_x = (Screen.winfo_screenwidth() - total_width) // 2

    input_lang_label = Label(Screen, text="Input Language", font="arial 12", bg="#D6D5D6")
    input_lang_label.place(x=button_x, y=70)

    output_lang_label = Label(Screen, text="Translated Language", font="arial 12", bg="#D6D5D6")
    output_lang_label.place(x=button_x + button_width_small + space_between_buttons, y=70)

    Input_lang_button = OptionMenu(Screen, Input_lang, *Languages)
    Input_lang_button.place(x=button_x, y=100, width=button_width_small, height=button_height_small)
    Input_lang_button.config(fg="black", highlightcolor="red", highlightbackground= "#47cbed", activebackground="black", activeforeground="#47cbed", font="arial 12")

    Output_lang_button = OptionMenu(Screen, Output_lang, *Languages, command=lambda x: Translate())
    Output_lang_button.place(x=button_x + button_width_small + space_between_buttons, y=100, width=button_width_small, height=button_height_small)
    Output_lang_button.config(fg="black", highlightcolor="#47cbed", highlightbackground= "#47cbed", activebackground="black", activeforeground="#47cbed", font="arial 12")


    def Translate():
        translator = Translator(from_lang = Input_lang.get(), to_lang = Output_lang.get())
        Translation = translator.translate(TextVar.get())
        OutputVar.set(Translation)
        play_audio(OutputVar.get(), Output_lang.get())


    #########################     TRANSLATE AND EXIT BUTTON SECTION    ########################
    # Adjust the button width and height for Input_lang and Output_lang buttons
    button_width_medium = 200
    button_height_medium = 40
    space_between_buttons = 100  # Adjust this value for the desired space

    # Calculate the total width required for both buttons and the space
    total_width = 2 * button_width_medium + space_between_buttons

    # Calculate the x-coordinate to center the buttons and space
    button_x = (Screen.winfo_screenwidth() - total_width) // 2

    translate_icon = Image.open("C:\\Users\\Adedolapo.Olutuyo\\Documents\\ISW_TA\\python\\translate.png")
    translate_icon = translate_icon.resize((32, 32))
    translate_photo = ImageTk.PhotoImage(translate_icon)
    
    speak_icon = Image.open("C:\\Users\\Adedolapo.Olutuyo\\Documents\\ISW_TA\\python\\user-voice-regular-24.png")
    speak_icon = speak_icon.resize((32, 32))
    speak_photo = ImageTk.PhotoImage(speak_icon)
    
    clear_icon = Image.open("C:\\Users\\Adedolapo.Olutuyo\\Documents\\ISW_TA\\python\\clear.png")
    clear_icon = clear_icon.resize((32, 32))
    clear_photo = ImageTk.PhotoImage(clear_icon)

    exit_icon = Image.open("C:\\Users\\Adedolapo.Olutuyo\\Documents\\ISW_TA\\python\\exit.png")
    exit_icon = exit_icon.resize((32, 32))
    exit_photo = ImageTk.PhotoImage(exit_icon)

    translate_button = Button(Screen, image=translate_photo, compound="left", text="Translate", font="arial 12", bg="#47cbed", command=Translate)
    translate_button.image = translate_photo
    translate_button.place(x=button_x - 310 , y=580, width=button_width_medium, height=button_height_medium)

    speak_again_button = Button(Screen, image=speak_photo, compound="left", text="Play Response Again", font="arial 12", bg="#47cbed", command=lambda: play_audio(OutputVar.get(), Output_lang.get()))
    speak_again_button.image = speak_photo
    speak_again_button.place(x=button_x, y=580, width=button_width_medium, height=button_height_medium)

    clear_button = Button(Screen, image=clear_photo, compound="left", text="Clear", font="arial 12", bg="#47cbed", command=clear_text)
    clear_button.image = clear_photo
    clear_button.place(x=button_x + button_width_medium + space_between_buttons, y=580, width=button_width_medium, height=button_height_medium)

    exit_button = Button(Screen, image=exit_photo, compound="left", text="Exit", font="arial 12", bg="red", fg="#ffffff", command=exit_program)
    exit_button.image = exit_photo
    exit_button.place(x=button_x + 2 * (button_width_medium + space_between_buttons), y=580, width=button_width_medium, height=button_height_medium)

    Screen.mainloop()


# Create a splash screen
splash = Tk()
splash.title("Intro Animation")
splash.attributes("-fullscreen", True)
splash.configure(bg="#808A87")

# Create a canvas to draw the animation
canvas = Canvas(splash, bg="#808A87", highlightthickness=0)
canvas.pack(fill="both", expand=True)

labels = [
    {"text": "Quantum\n", "x": -200, "y": splash.winfo_screenheight() // 2, "speed": 30},
    {"text": "Translator\n", "x": -200, "y": splash.winfo_screenheight() // 2 + 100, "speed": 30},
]

animated_labels = []
for label_info in labels:
    label = canvas.create_text(
        label_info["x"],
        label_info["y"],
        text=label_info["text"],
        font=("Arial", 45, "bold"),
        fill="black"
    )
    animated_labels.append(label)

animate_labels()

splash.mainloop()