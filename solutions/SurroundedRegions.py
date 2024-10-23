from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_size = len(board)
        col_size = len(board[0])
        for r in range(row_size):
            if board[r][0] == 'O':
                self.boundary_connection_check(board, r, 0)
            if board[r][col_size - 1] == 'O':
                self.boundary_connection_check(board, r, col_size - 1)

        for c in range(col_size):
            if board[0][c] == 'O':
                self.boundary_connection_check(board, 0, c)
            if board[row_size - 1][c] == 'O':
                self.boundary_connection_check(board, row_size - 1, c)

        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

    def boundary_connection_check(self, board: List[List[str]], r, c) -> None:
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'O':
            return
        board[r][c] = '#'
        if r > 1 and board[r - 1][c] == 'O':
            self.boundary_connection_check(board, r - 1, c)
        if r < len(board) - 2 and board[r + 1][c] == 'O':
            self.boundary_connection_check(board, r + 1, c)
        if c > 1 and board[r][c - 1] == 'O':
            self.boundary_connection_check(board, r, c - 1)
        if c < len(board[0]) - 2 and board[r][c + 1] == 'O':
            self.boundary_connection_check(board, r, c + 1)


solution = Solution()
board = [["O", "O", "O", "O", "X", "X"], ["O", "O", "O", "O", "O", "O"], ["O", "X", "O", "X", "O", "O"],
         ["O", "X", "O", "O", "X", "O"], ["O", "X", "O", "X", "O", "O"], ["O", "X", "O", "O", "O", "O"]]
solution.solve(board)
print(board)
