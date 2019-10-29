import connect_four.connect_four as c4

grid = c4.Grid(6, 7)

grid.add_piece(0, 'x')
grid.add_piece(0, 'x')
grid.add_piece(0, 'x')
grid.add_piece(0, 'x')
grid.add_piece(1, 'x')
grid.add_piece(5, 'x')

print(grid.state())
print(grid.get_token_coordinates('x'))

print(grid.winning_lines())

# game = Game()
# game.print_grid()
# game.add_piece('a', 3)
# game.print_grid()

# [
#     'x',
#     [(0,0), (0,1), (0,2), (0,3)]
# ]