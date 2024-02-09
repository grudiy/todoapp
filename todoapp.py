# Added storing to the txt file

while True:
    user_action = input("Type: add, edit, show, done, exit: ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # now we need to strip '/n' from every item
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            # or just list comprehensions
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                row = f"{index + 1}.{item}"
                print(row)

        case "edit":
            number = int(input("Enter todo number for edit:"))
            number = number - 1
            print("Editing ", todos[number])
            new_todo = input("New value: ")
            todos[number] = new_todo
            print("Saved: ", todos[number])

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




