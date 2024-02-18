import PySimpleGUI as gui
import functions

label = gui.Text('Type in a ToDo')
input_box = gui.InputText(tooltip='Enter ToDo', key="todo")
choose_button = gui.Button('Add')

window = gui.Window('My ToDo App',
                    layout=[[label], [input_box, choose_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break

window.close()
