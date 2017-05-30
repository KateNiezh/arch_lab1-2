if __name__ == '__main__':

    from views import out_menu, read_number_of_menu_item
    from controllers import Controller

    controller = Controller()

    while True:
        out_menu()
        command = read_number_of_menu_item()
        if command.__contains__("key"):
            getattr(controller, command["action"])(command["key"])
        else:
            getattr(controller, command["action"])()
