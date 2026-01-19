FILEPATH = "todo.txt" #constants or variables

def get_todos(filepath): #filepath is called parameters
#def get_todos(filepath="todo.txt") here we are providing default parameter (check line 22)
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath,todos_arg):
    with open(filepath, 'w') as file2:
        file2.writelines(todos_arg)


if __name__ == "__main__":  #usually used to test code for this file
    print(get_todos("../Exercise/todo.txt"))