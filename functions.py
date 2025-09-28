def get_todos(filepath="todos.txt"):
    try:
        with open(filepath, 'r') as file:
            return file.readlines()

    except FileNotFoundError:
        print("file not found!")
        return None


def write_todos(filepath="todos.txt", newtodos=None):
    if newtodos is None:
        newtodos = []
    with open(filepath, 'w') as file:
        file.writelines(newtodos)

todos = get_todos('todos.txt')

if __name__ == "__main__":
    print("calling from main in functions.py")
    print(todos)
