import pytest
import connect_four.connect_four as c4

num_rows = 6
num_cols = 7

blank_grid = '''-------
-------
-------
-------
-------
-------
'''

def test_player_a_starts_the_game():
    game = c4.Game()

    assert game.turn == 'a'


def test_player_b_goes_after_player_a():
    game = c4.Game()

    assert game.turn == 'a'

def test_move_in_a_too_large_column_number_throws_indexError():
    grid = c4.Grid(num_rows, num_cols)
    
    with pytest.raises(IndexError):
        grid.add_piece(num_cols, 'x')

def test_move_in_a_full_column_throws_valueError():
    grid = c4.Grid(num_rows, num_cols)
    for i in range(num_rows):
        grid.add_piece(0, 'x')
    
    with pytest.raises(ValueError):
        grid.add_piece(0, 'x')

def test_reset_clears_existing_board_state():
    grid = c4.Grid(num_rows, num_cols)
    grid.add_piece(0, 'x')
    grid.add_piece(1, 'o')
    
    grid.reset()

    assert grid.state() == blank_grid