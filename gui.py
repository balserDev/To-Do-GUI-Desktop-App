import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To Do App", layout=[
    [label, input_box],
    [add_button]

], font=("Helvetica", 10))

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case"Add":
            todos = functions.readfile()
            todos.append(values["todo"] + "\n")
            functions.writefile("toDos.txt", todos)
        case sg.WIN_CLOSED:
            break

window.close()

