def get_todos(filepath="todos.txt"):
    """ Gets existing todos from the file. "todos.txt" is a default file path."""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_list, filepath="todos.txt"):
    """Writes todos to the file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_list)


while True:
    user_action = input("Type: add, show, edit(#), done(#), exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            print("Editing ", todos[number])
            new_todo = input("New value: ") + "\n"
            todos[number] = new_todo
            write_todos(todos)
            print("Saved: ", todos[number])
        except ValueError:
            print("You should enter number")
            continue
        except IndexError:
            print("There is no such number")
            continue

    elif user_action.startswith("done"):
        try:
            number = int(user_action[5:])
            index = number - 1
            todos = get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            message = f"Completed: {todo_to_remove}"
            print(message)
        except ValueError:
            print("You should enter number")
            continue
        except IndexError:
            print("There is no such number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command")
print("bye")
