import connect_four.connect_four as c4
from .exceptions import InvalidColumnError, ColumnFullError

class ConnectFourDriver:

    def __init__(self, **kwargs) -> None:
        self._game = c4.Game()
    
    def start(self):

        print('Welcome to Connect 4!')

        while(True):
            self._game.print()
            print()
            print('Turn to move: {}. Enter the column number to add your piece'.format(self._game.turn))
            
            # Get user input
            try:
                column = int(input())
            except ValueError:
                continue

            # Make the user's move
            try:
                self._game.move(column)
            except ColumnFullError:
                print('That column is already full. Try again.')
            except InvalidColumnError:
                print('That isn''t a valid column number. Try again.')
            
            if self._game.game_state == 'WIN':
                self._game.print()
                print('Player {} has won!'.format(self._game.winner))
                print(self._game.winning_lines)
                quit()
            if self._game.game_state == 'TIE':
                self._game.print()
                print('No moves left. The game is tie!')
                quit()
