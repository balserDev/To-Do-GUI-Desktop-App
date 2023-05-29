def readfile(filepath="toDos.txt"):
    """
    Reads the textfile and returns its content
    on the users list
    """
    with open(filepath, "r") as file_local:
        user_local = file_local.readlines()
    return user_local


def writefile(filepath, text):
    """
    This function writes the new items in the user list
    :param filepath: File where the text would be stored
    :param text: This is the users list
    :return:Nothing would be returned
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(text)


def get_time():
    import time
    current_date = time.strftime("%Y-%M-%d, %H:%M:%S")
    print(f" Today is: {current_date}")
