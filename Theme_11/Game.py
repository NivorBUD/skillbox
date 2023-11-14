class Cell:
    def __init__(self):
        self.used = False
        self.sym = ''


class Board:

    def __init__(self, size=3):
        self.size = size
        self.cells = [[Cell() for _ in range(self.size)] for _ in range(self.size)]

    def update_cell(self, row, column, sym):
        if not self.cells[row][column].used:
            self.cells[row][column].sym = sym
            self.cells[row][column].used = True
            return True
        else:
            return False

    def print_board(self):
        count = self.size ** 3
        for i in range(self.size):
            print('-' * count)
            out = '|\t'
            for j in range(self.size):
                out += str(self.cells[i][j].sym) + '\t|\t'
            print(out)
        print('-' * count)

    def check_game_over(self, sym):
        for row in range(self.size):
            if all(self.cells[row][column].sym == sym for column in range(self.size)):
                return True
        for column in range(self.size):
            if all(self.cells[row][column].sym == sym for row in range(self.size)):
                return True
        if (all(self.cells[index][index].sym == sym for index in range(self.size)) or
                all(self.cells[self.size - 1 - index][index].sym == sym for index in range(self.size))):
            return True
        return False


class Player:
    def __init__(self, name, player_sym):
        self.wins_count = 0
        self.name = name
        self.player_sym = player_sym

    def move(self, board):
        while True:
            choice = input(f'\nХодит {self.name}({self.player_sym}). '
                           f'Введите номер строки и столбца через пробел: ').split()
            if len(choice) == 2 and all(board.size >= int(num) > 0 for num in choice):
                row, column = int(choice[0]) - 1, int(choice[1]) - 1
                return row, column
            else:
                print('Ошибка ввода')


class Game:
    def __init__(self, players: list[Player], board=Board()):
        self.state = "Start Game"
        self.players = players
        self.board = board

    def start_move(self, player):
        while True:
            row, column = player.move(self.board)
            if self.board.update_cell(row, column, player.player_sym):
                break
            print('Данная клетка уже занята')
        self.board.print_board()
        if self.board.check_game_over(player.player_sym):
            print(f'Победил {player.name}')
            player.wins_count += 1
            return True
        else:
            return False

    def new_game(self):
        self.board.cells = [[Cell() for _ in range(self.board.size)] for _ in range(self.board.size)]

        for move_num in range(self.board.size * self.board.size):
            player = self.players[move_num % 2]
            if self.start_move(player):
                return True
        else:
            print('Ничья')
            return False

    def start_game(self):
        while True:
            self.new_game()
            print(f'У 1 игрока: {self.players[0].wins_count} побед, у 2 игрока: {self.players[1].wins_count} побед')
            choice = input('Хотите сыграть ещё? (y/n) ')
            if choice == 'n':
                break