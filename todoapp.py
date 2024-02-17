import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type: add, show, edit(#), done(#), exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            print("Editing ", todos[number])
            new_todo = input("New value: ") + "\n"
            todos[number] = new_todo
            functions.write_todos(todos)
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
            todos = functions.get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
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
