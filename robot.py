from table import Table


# Controls the robot and its behaviour, movement, direction etc
# Depends on the table class
class Robot:

    def __init__(self):
        self.current_y_position = None          # Robots y coordinate on the table
        self.current_x_position = None          # Robots x coordinate on the table
        self.direction = None                   # Robots direction (N/S/E/W)
        self.is_placed = False                  # Is the robot on the table?
        self.table_size = 5
        self.table = Table(self.table_size)     # The table the robot plays on

    # Places the robot on the table
    def place_robot(self, y, x, direction):
        y = -abs(y) - 1                         # Because (0,0) is bottom left corner, need to invert and -1 y coordinate
        self.table.table[y][x] = 'R'

        # Update attributes now robot is on the board
        self.set_current_y_position(-abs(y) - 1)
        self.set_current_x_position(x)
        self.set_direction(direction)
        self.set_is_placed()

    # Moves the robot 1 space in the direction it's facing
    def move_robot(self):
        direction = self.get_direction()
        current_y_position = self.get_current_y_position()
        current_x_position = self.get_current_x_position()

        match direction:
            case 'NORTH':
                pass
            case 'SOUTH':
                pass
            case 'EAST':
                pass
            case 'WEST':
                pass

    # Reports the robots position
    def report_position(self):
        pass

    # Checks a move is valid (Robot won't fall off edge)
    def validate_move(self, current_y_position, current_x_position, direction):
        match direction:
            case 'NORTH':
                pass
            case 'SOUTH':
                pass
            case 'EAST':
                pass
            case 'WEST':
                pass

    # Set methods
    def set_current_y_position(self, coordinate):
        self.current_y_position = coordinate

    def set_current_x_position(self, coordinate):
        self.current_x_position = coordinate

    def set_direction(self, direction):
        self.direction = direction

    def set_is_placed(self):
        self.is_placed = True

    # Get methods
    def get_direction(self):
        return self.direction

    def get_current_y_position(self):
        return self.current_y_position

    def get_current_x_position(self):
        return self.current_x_position

    def get_is_placed(self):
        return self.is_placed

    def get_table_size(self):
        return self.table_size