
def get_todos(filepath="todos.txt"):
    """ Gets existing todos from the file. "todos.txt" is a default file path."""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_list, filepath="todos.txt"):
    """Writes todos to the file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_list)

if __name__ == "__main__":
    print(get_todos())