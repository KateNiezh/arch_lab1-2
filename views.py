_menu = [

    {
        "id": "1",
        "command": "Get subscribers",
        "action": "get_all_subscribers"
    },
    {
        "id": "2",
        "command": "Add new subscriber",
        "action": "add_new_subscriber"
    },
    {
        "id": "3",
        "command": "Find subscriber by name",
        "action": "find_subscriber",
        "key": "subscriber"
    },
    {
        "id": "4",
        "command": "Find subscriber by phone",
        "action": "find_subscriber",
        "key": "phone"
    },
    {
        "id": "5",
        "command": "Update subscriber's name",
        "action": "update_subscriber",
        "key": "subscriber"
    },
    {
        "id": "6",
        "command": "Update subscriber's phone",
        "action": "update_subscriber",
        "key": "phone"
    },
    {
        "id": "7",
        "command": "Remove subscriber by name",
        "action": "delete_subscriber"
    },
    {
        "id": "8",
        "command": "Exit",
        "action": "save_and_exit"
    }

]


def read_number_of_menu_item():
    """
    wait for command from Console: command is the number of menu item
    to run it. After entering check entered data and, if command is valid,
    returns dict with command id, command title and action.
    Otherwise run itself again.
    """
    try:
        num = int(input('Enter command number:\n> '))
        if num <= 0 or num > len(_menu):
            return read_number_of_menu_item()
        return get_item(num)
    except ValueError:
        return read_number_of_menu_item()


def out_menu():
    """
    print Menu of program
    """
    for item in _menu:
        print(item["id"] + ") " + item["command"])


def get_item(command):
    """
    returns dict from _menu with command id, command title,
    controller and action by id
    """
    return next(item for item in _menu if item["id"] == str(command))


def out_subscribers_and_their_phone_numbers(subscribers):
    """
    print subscribers as
    Name: subscriber's name
    Phone: suscriber's phone number
    ...
    """
    if len(subscribers) == 0 or subscribers == [None]:
        print("\nDatabase is empty")
        return
    print("")
    for sub in subscribers:
        print("Name: " + sub["subscriber"] + "\nPhone: " + sub["phone"] + "\n")
    input("Press any key to continue\n")


def enter_subscriber():
    """
    read new subscriber's name from Console.
    Return name
    """
    sub = input("Enter subscriber\'s name:\n> ")
    if len(sub) == 0:
        return enter_subscriber()
    return sub


def enter_phone_number():
    """
    read new subscriber's phone number from Console.
    Return phone number
    """
    number = input("Enter phone number\'s name:\n> ")
    if len(number) == 0:
        return enter_phone_number()
    return number


def enter_new_subscriber_and_phone_number():
    """
    call enter_subscriber(), enter_phone_number() and return their results
    """
    return enter_subscriber(), enter_phone_number()


def print_result_of_adding(index):
    """
    print message result of adding
    """
    print_message(
        index,
        "Subscriber successfully added",
        "Subscriber already exists")


def print_result_of_updating(index):
    """
    print message result of updating
    """
    print_message(
        index,
        "Subscriber successfully updated",
        "Subscriber error while updating")


def print_result_of_deleting(index):
    """
    print message result of deleting
    """
    print_message(
        index,
        "Subscriber successfully deleted",
        "Subscriber error while deleting")


def print_message(index, message1, message2):
    """
    print message of operation. If index > 0, print message1,
    else print message2.
    """
    if index > 0:
        print(message1)
    else:
        print(message2)
