
while True:
    user_action = input("Type: add, edit(#), show, done, exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            print("Editing ", todos[number])
            new_todo = input("New value: ") + "\n"
            todos[number] = new_todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Saved: ", todos[number])
        except ValueError:
            print("You should enter number")
            continue

    elif user_action.startswith("done"):
        try:
            number = int(user_action[5:])
            index = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Completed: {todo_to_remove}"
            print(message)
        except IndexError:
            print("There is no such number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command")
print("bye")




