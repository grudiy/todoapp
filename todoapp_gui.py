import time
import PySimpleGUI as gui
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as f:
        pass

label_time = gui.Text('', key='label_time')
label_intro_text = gui.Text('Type in a ToDo')
input_box = gui.InputText(tooltip='Enter ToDo', key="todo_input")
choose_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.get_todos(), key="todo_list_item",
                       enable_events=True, size=(45, 20))
edit_button = gui.Button('Edit')

complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit')

my_layot = [[label_time],
            [label_intro_text],
            [input_box, choose_button],
            [list_box, edit_button, complete_button],
            [exit_button]]

window = gui.Window('My ToDo App', layout=my_layot, font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200)
    window['label_time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo_input'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_list_item'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todo_list_item'][0]
                new_todo = values['todo_input'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todo_list_item'].update(values=todos)
            except IndexError:
                gui.popup('Please choose element', font=('Helvetica', 16))

        case "Complete":
            try:
                todo_to_complete = values['todo_list_item'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_list_item'].update(values=todos)
                window['todo_input'].update(value="")
            except IndexError:
                gui.popup('Please choose element', font=('Helvetica', 16))

        case "Exit":
            break

        case "todo_list_item":
            window['todo_input'].update(value=values['todo_list_item'][0])

        case gui.WIN_CLOSED:
            break

window.close()
