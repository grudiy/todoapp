import PySimpleGUI as gui
import functions

label = gui.Text('Type in a ToDo')
input_box = gui.InputText(tooltip='Enter ToDo', key="todo_input")
choose_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.get_todos(), key="todo_list_item",
                       enable_events=True, size=(45,15))
edit_button = gui.Button('Edit')

complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit')

my_layot = [[label],
            [input_box, choose_button],
            [list_box, edit_button, complete_button],
            [exit_button]]

window = gui.Window('My ToDo App', layout=my_layot, font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo_list_item'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo_input'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo_list_item'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todo_list_item'][0]
            new_todo = values['todo_input'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todo_list_item'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todo_list_item'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todo_list_item'].update(values=todos)
            window['todo_input'].update(value="")

        case "Exit":
            break

        case "todo_list_item":
            window['todo_input'].update(value=values['todo_list_item'][0])

        case gui.WIN_CLOSED:
            break

window.close()
