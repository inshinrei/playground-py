from functools import lru_cache
import math


def find(board, hand):
    def de(_board):
        start = 0
        for i, c in enumerate(_board):
            if c != _board[start]:
                if i - start >= 3:
                    return de(_board[:start] + _board[i:])
            start = i
        return _board

    @lru_cache(None)
    def dfs(_board, _hand):
        _board = de(_board)
        if _board == '#':
            return 0
        board_set = set(_board)
        _hand = ''.join(h for h in _hand if h in board_set)
        output = math.inf
        if not _hand:
            return result
        for i in range(len(_board)):
            for j, h in enumerate(_hand):
                new_hand = _hand[:j] + _hand[j + 1:]
                new_board = _board[:i] + h + _board[i:]
                output = min(output, 1 + dfs(new_board, new_hand))
        return output

    result = dfs(board + '#', hand)
    return -1 if result == math.inf else result
