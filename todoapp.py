# work with file implemented

while True:
    user_action = input("Type: add, edit, show, done, exit: ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            # strip /n with the list comprehensions
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)

        case "edit":
            number = int(input("Enter todo number for edit:"))
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            print("Editing ", todos[number])
            new_todo = input("New value: ") + "\n"
            todos[number] = new_todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Saved: ", todos[number])

        case "done":
            number = int(input("Enter todo number for complete:"))
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(number)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Completed.")

        case "exit":
            break
        case _:
            print("Invalid choice")

print("bye")




