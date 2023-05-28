from queue import PriorityQueue

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} |')
            print('-------------')

    def is_winner(self, player):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] == player:
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def get_empty_cells(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    def make_move(self, move, player):
        self.board[move] = player

    def undo_move(self, move):
        self.board[move] = ' '

    def evaluate(self):
        if self.is_winner('X'):
            return 1
        elif self.is_winner('O'):
            return -1
        else:
            return 0

    def get_best_move(self):
        moves = self.get_empty_cells()
        best_score = float('-inf')
        best_move = None

        for move in moves:
            self.make_move(move, self.current_player)
            score = self.minimax(False)
            self.undo_move(move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, is_maximizing):
        if self.is_winner('X'):
            return 1
        elif self.is_winner('O'):
            return -1
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_empty_cells():
                self.make_move(move, 'X')
                score = self.minimax(False)
                self.undo_move(move)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_empty_cells():
                self.make_move(move, 'O')
                score = self.minimax(True)
                self.undo_move(move)
                best_score = min(best_score, score)
            return best_score

    def play_game(self):
        while True:
            self.print_board()

            if self.is_winner('X'):
                print("You win!")
                break

            if self.is_board_full():
                print("It's a tie!")
                break

            if self.current_player == 'X':
                move = int(input("Enter your move (0-8): "))
                if move not in self.get_empty_cells():
                    print("Invalid move. Try again.")
                    continue
            else:
                move = self.get_best_move()

            self.make_move(move, self.current_player)
            self.current_player = 'O' if self.current_player == 'X' else 'X'


# Create a Tic-Tac-Toe game instance
game = TicTacToe()

# Start the game
game.play_game()
