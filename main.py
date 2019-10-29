import connect_four.connect_four as c4
from connect_four import driver

grid = c4.Grid(6, 7)

# grid.add_piece(0, 'x')
# grid.add_piece(0, 'x')
# grid.add_piece(0, 'x')
# grid.add_piece(0, 'x')
# grid.add_piece(1, 'x')
# grid.add_piece(2, 'x')
# grid.add_piece(3, 'x')
# grid.add_piece(5, 'x')
# grid.add_piece(1, 'x')
# grid.add_piece(2, 'o')
# grid.add_piece(2, 'x')
# grid.add_piece(3, 'o')
# grid.add_piece(3, 'o')
# grid.add_piece(3, 'x')
# grid.add_piece(0, 'x')

# print(grid.state())
# print(grid.get_token_coordinates('x'))

# print(grid.winning_lines())

# game = Game()
# game.print_grid()
# game.add_piece('a', 3)
# game.print_grid()

# [
#     'x',
#     [(0,0), (0,1), (0,2), (0,3)]
# ]

game = c4.Game()
game.move(3)
game.move(3)
game.move(3)
game.move(3)
game.move(3)
game.move(3)

driver = driver.ConnectFourDriver()
driver.start()