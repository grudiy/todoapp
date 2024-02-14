
while True:
    user_action = input("Type: add, edit, show, done, exit: ")

    if "add" in user_action:
        todo = user_action[4:] + '\n'
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        # strip /n with the list comprehensions
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif "edit" in user_action:
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

    elif "done" in user_action:
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

    elif "exit" in user_action:
        break

    else:
        print("Invalid command")
print("bye")




