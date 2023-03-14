import numpy as np

with open('./input.txt', encoding='utf-8') as input_data:
    def is_win(board):
        return np.any(np.sum(board, axis=1) == -board.shape[0]) or np.any(np.sum(board, axis=0) == -board.shape[1])


    def score(board):
        return np.sum(board[board != -1])


    data = input_data.read().splitlines()
    drawn = [int(r) for r in data[0].split(',')]
    players = 6
    total_boards_count = (len(data) - 1) // players
    boards = []
    for i in range(total_boards_count):
        board = [(list(int(r) for r in data[i * 6 + j + 2].split())) for j in range(5)]
        boards.append(np.array(board))

    for d in drawn:
        for i, b in enumerate(boards):
            X, Y = b.shape
            for x in range(X):
                for y in range(Y):
                    if b[x, y] == d:
                        b[x, y] = -1
                        if is_win(b):
                            print(f'board {i} win with score {score(b)}')
                            assert score(b) * d == 10374
                            exit()
