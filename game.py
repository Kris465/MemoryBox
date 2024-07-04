import tkinter as tk

class TicTacToeBoard(tk.Frame):
    def __init__(self, master, board_size=3, player='X'):
        super().__init__(master)
        self.master = master
        self.board_size = board_size
        self.buttons = []
        self.player = player
        self.game_over = False

        self.create_board()

    def create_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(self, text='', width=10, height=3,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def check_winner(self):
        # Проверяем выигрышные комбинации
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in lines:
            symbols = [self.buttons[i]['text'] for i in line]
            if symbols == ['X', 'X', 'X'] or symbols == ['O', 'O', 'O']:
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def clear_board(self):
        for button in self.buttons:
            button.config(text='')

    def restart_game(self):
        self.clear_board()
        self.player = 'X'
        self.game_over = False

    def on_click(self, row, col):
        if self.game_over:
            return

        button_index = row * self.board_size + col
        self.buttons[button_index].config(text=self.player)
        
        if self.check_winner():
            print(f'Player {self.player} wins!')
            self.disable_buttons()
            self.game_over = True

        # После каждого хода меняем игрока
        self.player = 'O' if self.player == 'X' else 'X'




class TicTacToeGame:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('TicTacToe')

        player_choice = tk.StringVar(value='X')
        player_select_label = tk.Label(self.root, text='Select Player (X or O): ')
        player_select_label.pack()
        
        player_select_entry = tk.Entry(self.root, textvariable=player_choice)
        player_select_entry.pack()

        start_button = tk.Button(self.root, text='Start Game', command=lambda: self.start_game(player_choice.get()))
        start_button.pack()

    def start_game(self, player):
        self.board = TicTacToeBoard(self.root, player=player)
        self.board.pack()

    def run(self):
        self.root.mainloop()
