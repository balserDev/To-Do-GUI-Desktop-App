# import functions
from functions import readfile, writefile, get_time

get_time()

while True:
    # Gets first user input
    User_Action = input("Want do you want to do? (Type comands for options)")
    User_Action = User_Action.strip()

    if User_Action.startswith("Comands") or "comands" in User_Action:
        print("Add,Show,Edit,Exit,Completed")

    elif User_Action.startswith("Add") or "add" in User_Action:
        ToDo = User_Action[4:] + "\n"

        User_List = readfile("ToDos.txt")

        User_List.append(ToDo.capitalize())
        print(f"{ToDo} was successfully added to your list")

        writefile("ToDos.txt", User_List)

    elif User_Action.startswith("Show") or "show" in User_Action:

        User_List = readfile("ToDos.txt")

        if len(User_List) == 0:
            print("No Tasks Have Been Added")
        else:

            new_toDos = [item.strip("\n") for item in User_List]

            for index, x in enumerate(new_toDos):
                x = x.title()
                print(f"{index +1 }-{x}")

    elif User_Action.startswith("Edit") or "edit" in User_Action:
        try:
            User_List = readfile("ToDos.txt")

            number = int(input("Item Number to be edited: "))
            number_edit = input("Type The New Content: ")
            User_List[number - 1] = number_edit + "\n"

            writefile("ToDos.txt", User_List)
        except ValueError:
            print("Wrong type of input")
            continue
        except IndexError:
            print("There is not a list item with that number")
            continue

    elif "Complete" in User_Action or "complete" in User_Action\
            or "Completed" in User_Action or "completed" in User_Action:
        try:
            # Otra forma de abrir y leer documentos de texto

            User_List = readfile("ToDos.txt")

            number = int(input("Enter Task To Be Completed: "))
            User_List.pop(number-1)

            writefile("ToDos.txt", User_List)

            print("The task was succesfully deleted")

        except ValueError:
            print("Wrong type of input")
            continue
        except IndexError:
            print("There is not a list item with that number")
            continue

    elif "Clear" in User_Action or "clear" in User_Action:

        User_List = readfile("ToDos.txt")

        User_List.clear()
        print("The list have been cleared")

        writefile("ToDos.txt", User_List)

    elif "Exit" in User_Action or "exit" in User_Action\
            or "Stop" in User_Action or "stop" in User_Action:
        break
    else:
        print("Not valid input, Try Again")


print("Thank you for using this software!!!")
