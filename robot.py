from table import Table


# Controls the robot and its behaviour, movement, direction etc
# Depends on the table class
class Robot:

    def __init__(self):
        self.current_y_position = None  # Robots y coordinate on the table
        self.current_x_position = None  # Robots x coordinate on the table
        self.direction = None  # Robots direction (N/S/E/W)
        self.is_placed = False  # Is the robot on the table?
        self.table_size = 5  # The size of the table, can be changed but is 5x5 for this program
        self.table = Table(self.table_size)  # The table the robot plays on
        self.valid_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

    # Places the robot on the table
    def place_robot(self, x, y, direction):
        table_size = self.get_table_size()
        y = -abs(y) - 1  # Because (0,0) is bottom left corner, need to invert and -1 y coordinate

        # Verify that the placement is not invalid (out of bounds) and that direction is valid
        if x < 0 or x > table_size or y > -1 or y < -abs(table_size):
            pass
        elif direction not in self.get_valid_directions():
            pass
        else:
            self.table.table[y][x] = 'R'

            # Update attributes now robot is on the board
            self.set_current_y_position(y)
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
                if self.validate_move(current_y_position, current_x_position, direction):
                    self.set_current_y_position(current_y_position - 1)
            case 'SOUTH':
                if self.validate_move(current_y_position, current_x_position, direction):
                    if current_y_position + 1 == 0:
                        pass
                    else:
                        self.set_current_y_position(current_y_position + 1)
            case 'EAST':
                if self.validate_move(current_y_position, current_x_position, direction):
                    self.set_current_x_position(current_x_position + 1)
            case 'WEST':
                if self.validate_move(current_y_position, current_x_position, direction):
                    self.set_current_x_position(current_x_position - 1)

        # Once robot has moved table needs to be updated to reflect the new position
        self.update_table()

    # Checks a move is valid (Robot won't fall off edge)
    # Returns false if move is out of bounds, else returns true
    def validate_move(self, current_y_position, current_x_position, direction):
        table_size = self.get_table_size()
        match direction:
            case 'NORTH':
                if (current_y_position - 1) < (-abs(table_size)):
                    return False
                else:
                    return True
            case 'SOUTH':
                if (current_y_position + 1) > 0:
                    return False
                else:
                    return True
            case 'EAST':
                if (current_x_position + 1) > (table_size - 1):
                    return False
                else:
                    return True
            case 'WEST':
                if (current_x_position - 1) < 0:
                    return False
                else:
                    return True

    # Rotate the robot left
    def rotate_robot(self, rotate_direction):
        direction_index = None
        new_direction = None

        current_direction = self.get_direction()
        directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

        # Retrieve the index of the current direction
        for i in range(len(directions)):
            if directions[i] == current_direction:
                direction_index = i

        if rotate_direction == "LEFT":
            new_direction = directions[direction_index - 1]
        elif rotate_direction == "RIGHT":
            if direction_index + 1 >= len(directions):  # If at end of array need to return to index 0 (East -> North)
                new_direction = directions[0]
            else:
                new_direction = directions[direction_index + 1]

        self.set_direction(new_direction)

    # Reports the robots position
    def report_position(self):
        if not self.get_is_placed():     # Verify that the robot has been placed
            output = "Robot Not Yet Placed"
        else:
            current_x_position = self.get_current_x_position()
            current_y_position = abs(self.get_current_y_position() + 1)      # Need to convert back into positive int for readability
            current_direction = self.get_direction()

            output = f'{current_x_position},{current_y_position},{current_direction}'

        return output

    # Updates the table by creating a new blank table and adding the robots position in
    # Should be called after an update to the robots position
    def update_table(self):
        table_size = self.get_table_size()
        current_y_position = self.get_current_y_position()
        current_x_position = self.get_current_x_position()
        new_table = Table(table_size)
        new_table.table[current_y_position][current_x_position] = 'R'
        self.set_table(new_table)

    # Set methods
    def set_current_y_position(self, coordinate):
        self.current_y_position = coordinate

    def set_current_x_position(self, coordinate):
        self.current_x_position = coordinate

    def set_direction(self, direction):
        self.direction = direction

    def set_is_placed(self):
        self.is_placed = True

    def set_table(self, table):
        self.table = table

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

    def get_valid_directions(self):
        return self.valid_directions
