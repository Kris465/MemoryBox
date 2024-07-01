import tkinter as tk


class TicTacToeBoard(tk.Frame):
    def __init__(self, master, board_size=3):
        super().__init__(master)
        self.master = master
        self.board_size = board_size
        self.buttons = []

        self.create_board(self)

    def create_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self, text='', width=10, heigth=3,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_click(self, row, col):
        button_index = row * self.board_size + col
        self.buttons[button_index].config(text='X')


class TicTacToeGame:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('TicTacToe')

        self.board = TicTacToeBoard(self.root)
        self.board.pack()

    def run(self):
        self.root.mainloop()
