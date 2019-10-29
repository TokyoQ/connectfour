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
            raise IndexError('Not a valid column number: {}'.format(column_number))

        row_number = len(self._cols[column_number])
        if row_number not in range(self.num_rows):
            raise ValueError('Column is already full. Cannot add a piece here.')
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
    
    # Check if the grid is in an end state
    def winning_lines(self):
        winning_lines = []
        
        for row_num in range(len(self._rows)):
            for col_num in range(len(self._cols)):
                token = self._rows[row_num][col_num]
                if token == self.blank_char:
                    continue
                if col_num + self.winning_number < len(self._cols):
                    # Check the horizontal
                    token_count = 1
                    winning_tokens = [(row_num, col_num)]

                    for i in range(1, self.winning_number):
                        test_token = self._rows[row_num][col_num+i]
                        if test_token == token:
                            token_count += 1
                            winning_tokens.append((row_num, col_num+i))
                    if token_count == self.winning_number:
                        winning_lines.append({'token': token, 'coords': winning_tokens})

                    if row_num + self.winning_number < len(self._rows):
                        # Check the diagonal
                        token_count = 1
                        winning_tokens = [(row_num, col_num)]

                        for i in range(1, self.winning_number):
                            test_token = self._rows[row_num+i][col_num+i]
                            if test_token == token:
                                token_count += 1
                                winning_tokens.append((row_num+i, col_num+i))
                        if token_count == self.winning_number:
                            winning_lines.append({'token': token, 'coords': winning_tokens})

                if row_num + self.winning_number < len(self._rows):
                    # Check the vertical
                    token_count = 1
                    winning_tokens = [(row_num, col_num)]

                    for i in range(1, self.winning_number):
                        test_token = self._rows[row_num+i][col_num]
                        if test_token == token:
                            token_count += 1
                            winning_tokens.append((row_num+i, col_num))
                    if token_count == self.winning_number:
                        winning_lines.append({'token': token, 'coords': winning_tokens})

        return winning_lines
        


class Game:    

    # Return the player who's turn it is
    @property
    def turn(self):
        return self.turn

    @property
    def grid_state(self):
        return self._grid.state()

    def __init__(self, **kwargs) -> None:
        num_rows = 6
        num_cols = 7
        self.players = ['a', 'b']
        self.tokens = {'a': 'x',
              'b': 'o'}

        self._grid = Grid(num_rows, num_cols)
        self.turn = 'a'

    # Take the player's move in the given column
    def move(self, column_number):
        token = self.tokens[self.turn]
        self._grid.add_piece(column_number, token)
