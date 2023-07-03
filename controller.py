from robot import Robot
import re


class Controller:

    def __init__(self):
        self.robot = Robot()

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
                case 'EXIT':
                    self.exit_program()

    # Handles moving the robot
    def control_move_robot(self):
        self.robot.move_robot()

    # Handles turning the robot
    def control_rotate_robot(self, rotate_direction):
        self.robot.rotate_robot(rotate_direction)

    # Handles reporting the robots position
    def control_report_robot(self):
        self.robot.report_position()

    # Handles placing the robot (command includes int and strings so bit messy)
    def control_place_robot(self, user_command):
        user_command = re.split(r',| ', user_command)

        user_command[1] = int(user_command[1])  # Need to convert coordinates to int
        user_command[2] = int(user_command[2])  # Need to convert coordinates to int

        self.robot.place_robot(user_command[1], user_command[2], user_command[3])

    # Will terminate the program when called
    @staticmethod
    def exit_program():
        quit()

    # The loop that allows the user to continuously enter commands
    def control_loop(self):
        while True:
            self.process_user_command()
