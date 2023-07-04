from robot import Robot
import re


class Controller:

    def __init__(self):
        self.robot = Robot()

    @staticmethod
    def list_commands():
        output = "PLACE X,Y,DIRECTION | LEFT | RIGHT | MOVE | REPORT | DISPLAY TABLE | EXIT"
        print(output)

    @staticmethod
    def get_user_command():
        user_command = input("Enter Command: ")
        return user_command

    def process_user_command(self):
        user_command = self.get_user_command()
        if 'PLACE' in user_command:
            self.control_place_robot(user_command)
        else:
            match user_command:
                case 'MOVE':
                    self.control_move_robot()
                case 'LEFT':
                    self.control_rotate_robot(user_command)
                case 'RIGHT':
                    self.control_rotate_robot(user_command)
                case 'REPORT':
                    self.control_report_robot()
                case 'DISPLAY TABLE':
                    self.control_display_table()
                case 'EXIT':
                    self.exit_program()
                # Used for testing purposes only
                case 'X':
                    print(self.robot.get_current_x_position())
                case 'Y':
                    print(self.robot.get_current_y_position())

    # Handles moving the robot
    def control_move_robot(self):
        self.robot.move_robot()

    # Handles turning the robot
    def control_rotate_robot(self, rotate_direction):
        self.robot.rotate_robot(rotate_direction)

    # Handles reporting the robots position
    def control_report_robot(self):
        print(self.robot.report_position())

    # Handles placing the robot (command includes int and strings so bit messy)
    def control_place_robot(self, user_command):
        user_command = re.split(r',| ', user_command)

        user_command[1] = int(user_command[1])  # Need to convert coordinates to int
        user_command[2] = int(user_command[2])  # Need to convert coordinates to int

        self.robot.place_robot(user_command[1], user_command[2], user_command[3])

    # Controls displaying the current table
    def control_display_table(self):
        self.robot.table.print_table()

    # Will terminate the program when called
    @staticmethod
    def exit_program():
        quit()

    # The loop that allows the user to continuously enter commands
    # Only used for human interaction, not required for testing
    def control_loop(self):
        while True:
            self.process_user_command()
