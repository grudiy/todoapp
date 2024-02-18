import PySimpleGUI as gui

label = gui.Text('Type in a ToDo')
input_box = gui.InputText(tooltip='Enter ToDo')
choose_button = gui.Button('Add')


window = gui.Window('My ToDo App',
                    layout=[[label, input_box, choose_button]])
window.read()
window.close()
