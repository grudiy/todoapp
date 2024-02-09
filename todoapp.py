todos = []
while True:
    user_action = input("Type: add, edit, show, exit: ")
    match user_action:
        case "add":
            user_input = input("Enter a todo: ")
            todos.append(user_input)
            print("Added: ", user_input)
        case "edit":
            todo_number = input("Enter todo number:")
            todo_number = int(todo_number) - 1
            print("Editing ", todos[todo_number])
            new_todo = input("New value: ")
            todos[todo_number] = new_todo
            print("Saved: ", todos[todo_number])
        case "show":
            for item in todos:
                print(todos.index(item) + 1, ": ",  item)
        case "exit":
            break
        case _:
            print("Invalid choice")

print("bye")






