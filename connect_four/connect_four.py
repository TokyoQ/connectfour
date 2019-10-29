import connect_four.exceptions as c4Errors
from .exceptions import InvalidColumnError, ColumnFullError

class Grid:

    def __init__(self, num_rows, num_cols, blank_char='-', **kwargs) -> None:
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.blank_char = blank_char
        self.winning_number = 4
        self.reset()

    # Reset the board state to blank
    def reset(self):
        self._rows = [[self.blank_char] * self.num_cols for i in range(self.num_rows)]
        self._cols = [[] for i in range(self.num_cols)]
        self.num_moves = 0
    
    # Return the board state as a readable string
    def state(self):
        state = ''
        for row in reversed(self._rows):
            state = state + ''.join(row) + '\n'
        return state
    
    # Get the token at the given position
    def value_at(self, row_number, column_number):
        return self._cols[column_number][row_number]
    
    # Add the specified token to a column
    def add_piece(self, column_number, token):
        if column_number not in range(self.num_cols):
            raise InvalidColumnError('Not a valid column number: {}'.format(column_number))

        row_number = len(self._cols[column_number])
        if row_number not in range(self.num_rows):
            raise ColumnFullError('Column is already full. Cannot add a piece here.')
        self._cols[column_number].append(token)
        self._rows[row_number][column_number] = token
    
    # Get the positions of the given tokens in the grid
    def get_token_coordinates(self, target_token):
        coords = []
        for row_num in range(len(self._rows)):
            for col_num in range(len(self._cols)):
                if self._rows[row_num][col_num] == target_token:
                    coords.append((row_num, col_num))
        return coords
    
    # Look for and return any winning lines
    def winning_lines(self):
        winning_lines = []
        
        for row_num in range(len(self._rows)):
            for col_num in range(len(self._cols)):
                token = self._rows[row_num][col_num]
                if token == self.blank_char:
                    continue
                if col_num + self.winning_number < len(self._cols):
                    # Check the horizontal
                    line = self.check_line(row_num, col_num, row_step=1, col_step=0)
                    if line is not None:
                        winning_lines.append(line)

                    if row_num + self.winning_number < len(self._rows):
                        # Check the diagonal
                        line = self.check_line(row_num, col_num, row_step=1, col_step=1)
                        if line is not None:
                            winning_lines.append(line)

                if row_num + self.winning_number < len(self._rows):
                    # Check the vertical
                    line = self.check_line(row_num, col_num, row_step=0, col_step=1)
                    if line is not None:
                        winning_lines.append(line)

        return winning_lines
    
    def check_line(self, row_start, col_start, row_step, col_step):
        token = self._rows[row_start][col_start]
        if token == self.blank_char:
            return None

        token_count = 1
        positions = []
        for i in range(1, self.winning_number-1):
            print('Orig token: Row {} | Col {}, Test token: Row {} | Col {}'.format(row_start, col_start, row_start + i*row_step, col_start + i*col_step))
            test_token = self._rows[row_start + i*row_step][col_start + i*col_step]
            if test_token == token:
                token_count += 1
                positions.append({'row': row_start + row_step, 'col': col_start + col_step})
            else:
                return None
        if token_count == self.winning_number:
            line = {'token': token, 'positions': positions}
            return line
        else:
            return None


class Game:    

    # Return the player who's turn it is
    @property
    def turn(self):
        return self._turn

    @property
    def state(self):
        return self._grid.state()
    
    def __init__(self, **kwargs) -> None:
        num_rows = 6
        num_cols = 7
        self.players = ['x', 'o']
        self.tokens = {'x': 'x', 'o': 'o'}
        self.next_turn = {'x': 'o', 'o': 'x'}

        self._grid = Grid(num_rows, num_cols)
        self._turn = 'x'

    # Print the grid state
    def print(self):
        grid = self._grid.state()
        output = '{}0123456'.format(grid)
        print(output)

    # Take the player's move in the given column
    def move(self, column_number):
        token = self.tokens[self.turn]
        self._grid.add_piece(column_number, token)

        winning_lines = self._grid.winning_lines()
        if len(winning_lines) > 0:
            return winning_lines
        
        self._turn = self.next_turn[self._turn]
        return None