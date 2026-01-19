from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to_do:")
input_box = sg.Input(tooltip="Enter a todo", key="to_do")
add_button = sg.Button("Add")

window = sg.Window('My To do App',
                   layout = [[label],[input_box,add_button]],
                   font   = ('Helvetica',15)

                   )
while True:
        event, values = window.read()
        print(values)
        match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values['to_do'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
            case sg.WIN_CLOSED:
                break

            
            

window.close()