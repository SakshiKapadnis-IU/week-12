import numpy as np

def update_board(board):
    """Perform one step of Conway's Game of Life on a binary NumPy array."""
    new_board = np.zeros_like(board)
    rows, cols = board.shape

    for r in range(rows):
        for c in range(cols):
            neighbors = board[max(0, r-1):min(rows, r+2),
                              max(0, c-1):min(cols, c+2)]
            live_neighbors = neighbors.sum() - board[r, c]

            if board[r, c] == 1:
                if live_neighbors in (2, 3):
                    new_board[r, c] = 1
            else:
                if live_neighbors == 3:
                    new_board[r, c] = 1

    return new_board

def recursive_game_of_life():
    """Play Conway's Game of Life recursively on a random 10x10 board."""
    board = np.random.randint(2, size=(10, 10))
    
    def step(board):
        return step(update_board(board))  # recursive call

    return step(board)