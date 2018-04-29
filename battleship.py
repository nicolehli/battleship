from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

# Hide the ship
ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
    if guess_row not in range(5) or guess_col not in range(5):
        "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
