import pytest
import connect_four.connect_four as c4

num_cols = 7
num_rows = 6

blank_grid = '''-------
-------
-------
-------
-------
-------
'''

def test_blank_grid_is_blank():
    grid = c4.Grid(num_rows, num_cols)

    assert grid.state() == blank_grid


def test_grid_tracks_one_move():
    grid = c4.Grid(num_rows, num_cols)
    grid.add_piece(3, 'x')

    assert grid.state() == '''-------
-------
-------
-------
-------
---x---
'''

    assert grid.value_at(0, 3) == 'x'

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