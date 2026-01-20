from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to_do:")
input_box = sg.Input(tooltip="Enter a todo", key="to_do")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='to_dos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To do App',
                   layout = [[label],[input_box,add_button],[list_box,edit_button]],
                   font   = ('Helvetica',15)

                   )
while True:
        event, values = window.read()
        print(event)
        print(values)
        match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values['to_do'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['to_dos'].update(values=todos)
            case "Edit":
                todo_to_edit = values['to_dos'][0]
                new_todo = values['to_do']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['to_dos'].update(values=todos)
            case "to_dos":
                window['to_do'].update(value=values['to_dos'][0])


            case sg.WIN_CLOSED:
                break

            
            

window.close()