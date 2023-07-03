class Controller:

    def __init__(self):
        self.y_coordinate = None
        self.x_coordinate = None
        self.direction = None
        self.action = None

    def get_user_command(self):
        user_command = input("Enter Command: ")
        if user_command.__contains__("PLACE"):
            pass


