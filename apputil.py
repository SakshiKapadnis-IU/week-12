import numpy as np

def update_board(board):
    """
    Perform one step of Conway's Game of Life on a binary NumPy array.
    
    Rules:
    - Any live cell with 2 or 3 live neighbors survives.
    - Any dead cell with exactly 3 live neighbors becomes alive.
    - All other cells die or remain dead.
    """
    # copy to avoid modifying original during neighbor counting
    new_board = np.zeros_like(board)
    rows, cols = board.shape

    # convolution-like neighbor count
    for r in range(rows):
        for c in range(cols):
            # count live neighbors
            neighbors = board[max(0, r-1):min(rows, r+2),
                              max(0, c-1):min(cols, c+2)]
            live_neighbors = neighbors.sum() - board[r, c]

            # apply rules
            if board[r, c] == 1:
                if live_neighbors in (2, 3):
                    new_board[r, c] = 1
            else:
                if live_neighbors == 3:
                    new_board[r, c] = 1

    return new_board


# OPTIONAL (NOT required, but helpful) – wrapper for the UI
def get_next_board(board):
    return update_board(board)