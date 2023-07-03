
# Controls the tablespace, uses a 2D array to represent a table
# x represents an unoccupied space, R represents that the robot is at that space
class Table:

    def __init__(self, table_size):
        # Creates a square 2d array of table size
        self.table = [['x'] * table_size for i in range(table_size)]

    # Outputs the table to the console in a nice format
    def print_table(self):
        for i in range(len(self.table)):
            output = ''
            for y in range(len(self.table)):
                output += self.table[i][y]
            print(output)