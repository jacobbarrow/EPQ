def get_next_move(tile_grid, army_grid, armies):
    """

    Inputs:
    ---
    tile_grid
    A 2D array with values -4 to 2 in each cell
    -4=Fog Obstacle; -3=Fog; -2=Mountain; -1=Empty Land; 0=Enemy; 1=Own; 2=Town
    ---
    army_grid
    A 2D array with army values of each square (0+)
    ---
    armies
    A tuple ({Own army size}, {Enemy army size})

    Returns:
    A tuple ((x, y), (x2, y2))
    (moving army from one coord to another)

    """

    return ((0, 0), (0,0)
