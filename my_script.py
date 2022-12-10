import math
import time
import random
from js import document, console
from pyodide.ffi import create_proxy

def rock_paper_scissors(*args, **kwargs):
        
            userInput = Element('rock-paper-scissors-input').element.value
            # user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
            computer = random.choice(['r', 'p', 's'])

            console.log(f'text: {userInput}')
        
            if userInput == computer:
                pyscript.write("result", 'It\'s a tie')
        
            # r > s, s > p, p > r
            if is_win(userInput, computer):
                pyscript.write("result",'You won!')
            
            else:
                pyscript.write("result",'You lost!')
        
def is_win(player, opponent):
            # return true if player wins
            # r > s, s > p, p > r
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
                or (player == 'p' and opponent == 'r'):
                return True
        
                
function_proxy = create_proxy(rock_paper_scissors)

document.getElementById("button").addEventListener("click", function_proxy)   







class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
             # each score should maximize
            best = {'position': None, 'score': -math.inf}
        else:
            # each score should minimize
            best = {'position': None, 'score': math.inf}
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            # simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            # this represents the move optimal next move
            sim_score['position'] = possible_move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        board = ""
        final = ""
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            board = board + '|  ' + '  |  '.join(row) + "  |  <br> " 
            final = board + "<br> <br>"
        document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + final
        print(board)

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        # number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        # for row in number_board:
        document.getElementById("tic-tac-toe-rules").innerHTML = "| 0 | 1 | 2 | <br> | 3 | 4 | 5 | <br> | 6 | 7 | 8 |"

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]



game = TicTacToe()



def playHumanPlayer(print_game=True):
    global game
    console.log(game.num_empty_squares())
    userInput = Element('tic-tac-toe-input').element.value
    document.getElementById("tic-tac-toe-input").value = ""
    if game.num_empty_squares() == 9:
        document.getElementById("tic-tac-toe-result").innerHTML = ""
    if len(userInput) < 1 :  
        document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + "Please insert a  value" + "<br>"
        return
    else:
        valid_square = False
        val = None
        while not valid_square:
            try:
                val = int(userInput)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + 'Invalid square. Try again.' + "<br>"
                return
        square = val
        if game.make_move(square, 'O'):
            if print_game:
                document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + 'O' + ' makes a move to square {}'.format(square) + "<br>"
                game.print_board()

            if game.current_winner:
                if print_game:
                   document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + 'O' + ' wins!'
                return 'O'  # ends the loop and exits the game
        time.sleep(1)
        square = SmartComputerPlayer('X').get_move(game)
        if game.make_move(square, 'X'):
            if print_game:
                document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + 'X' + ' makes a move to square {}'.format(square) + "<br>"
                game.print_board()

            if game.current_winner:
                if print_game:
                    document.getElementById("tic-tac-toe-result").innerHTML =  document.getElementById("tic-tac-toe-result").innerHTML + 'X' + ' wins!'
                    game = TicTacToe()
                return 'X'  # ends the loop and exits the game






def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()



if __name__ == '__main__':
    document.getElementById("tic-tac-toe-result").innerHTML = "Input your initial position in the board to start the game"
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

def playAgain(*args, **kwargs):
    global game
    game = TicTacToe()
    console.log("test")
    document.getElementById("tic-tac-toe-result").innerHTML = "Input any position to start"
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

Play_Again = create_proxy(playAgain)

Player_makes_move = create_proxy(playHumanPlayer)

document.getElementById("button-tic-tac-toe").addEventListener("click", Play_Again)

document.getElementById("Submit-square-tic-tac-toe").addEventListener("click", Player_makes_move)