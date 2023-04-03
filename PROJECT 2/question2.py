import PySimpleGUI as sg
import qrcode

sg.theme('GreenMono')   # Set the theme for the UI

# Define the layout for the app
layout = [[sg.Text('Enter Text: '), sg.InputText()],
          [sg.Button('Create'), sg.Button('Exit')], 
          [sg.Image(key='-IMAGE-', size=(200, 150))]]

# Create the window
window = sg.Window('QR Code Generator', layout)


# Event loop for the app
while True:
    event, values = window.read()   # Read events and values from the window

    if event in (sg.WIN_CLOSED, 'Exit'):   # If the Exit button or window is closed, exit the app
        break

    if event == 'Create':   # If the Create button is clicked, generate the QR code image
        data = values[0]   # Get the text input from the user
        if data:   # If the text input is not empty, generate the QR code
            img = qrcode.make(data)   # Generate the QR code image
            img.save('qrcode.png')   # Save the QR code image to a file
            window['-IMAGE-'].update(filename='qrcode.png')   # Update the image in the UI

# Close the window and exit the app
window.close()