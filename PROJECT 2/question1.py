import PySimpleGUI as sg
import pyttsx3

layout = [
    [sg.Text("Enter text to speak:")],
    [sg.Input(key="-INPUT-")],
    [sg.Text("Select voice type:")],
    [sg.Radio("Male", "RADIO1", key="-MALE-"), sg.Radio("Female", "RADIO1", key="-FEMALE-", default=True)],
    [sg.Button("Speak"), sg.Button("Exit")]
]

window = sg.Window("Text-to-Speech App", layout)

engine = pyttsx3.init()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Speak":
        text = values["-INPUT-"]
        male_voice = values["-MALE-"]     

        if male_voice:
            engine.setProperty('voice', 'english-male')
        else:
            engine.setProperty('voice', 'english-female')

        engine.say(text)
        engine.runAndWait()

window.close()