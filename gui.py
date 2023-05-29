import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to do", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
lis_box = sg.Listbox(values=functions.readfile(), key="todos",
                     enable_events=True, size=[45, 10])

window = sg.Window("My To Do App", layout=[
    [label],
    [input_box, add_button],
    [lis_box],
    [edit_button]
], font=("Helvetica", 10))

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case"Add":
            todos = functions.readfile()
            todos.append(values["todo"] + "\n")
            functions.writefile("toDos.txt", todos)

            window["todos"].update(values=todos)
        case"Edit":
            todos = functions.readfile()

            todo_edit = values["todos"][0]
            new_todo = values["todo"]

            index = todos.index(todo_edit)
            todos[index] = new_todo + "\n"

            functions.writefile("toDos.txt", todos)

            print(values["todos"])

            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()

