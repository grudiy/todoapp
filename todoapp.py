todos = []
while True:
    user_action = input("Type: add, edit, show, done, exit: ")
    match user_action:
        case "add":
            user_input = input("Enter a todo: ")
            todos.append(user_input)
            print("Added: ", user_input)

        case "edit":
            number = int(input("Enter todo number for edit:"))
            number = number - 1
            print("Editing ", todos[number])
            new_todo = input("New value: ")
            todos[number] = new_todo
            print("Saved: ", todos[number])

        case "show":
            for index, item in enumerate(todos):
                #f - strings
                row = f"{index + 1}-{item}"
                print(row)

        case "done":
            number = int(input("Enter todo number for complete:"))
            number = number - 1
            todos.pop(number)
            print("Completed.")

        case "exit":
            break
        case _:
            print("Invalid choice")

print("bye")




