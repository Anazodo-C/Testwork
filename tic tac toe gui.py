import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.player_turn = False  # Player starts second, computer starts first

        self.computer_move()  # Computer makes the first move

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="play", font=("Arial", 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.player_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def player_move(self, row, col):
        if self.board[row][col] == " " and not self.player_turn:
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")
            if self.check_winner() == "O":
                self.end_game("You win!")
            elif self.is_full():
                self.end_game("It's a tie!")
            else:
                self.player_turn = True
                self.computer_move()

    def computer_move(self):
        move = self.find_best_move()
        if move:
            row, col = move
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X")
            if self.check_winner() == "X":
                self.end_game("Computer wins!")
            elif self.is_full():
                self.end_game("It's a tie!")
            self.player_turn = False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.master.quit()

    def find_best_move(self):
        best_score = float('-inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "X"
                    score = self.minimax(0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        if winner == "X":
            return 1
        elif winner == "O":
            return -1
        elif self.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "X"
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "O"
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
