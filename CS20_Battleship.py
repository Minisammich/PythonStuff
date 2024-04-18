from random import randint

board = []

board.append([" ", "0", "1", "2", "3", "4"])
counter = 0
for x in range(0, 5):
  if counter == counter:
    strcounter = str(counter)
  board.append([strcounter, "O", "O", "O", "O", "O"])
  counter += 1

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, 4)

def random_col(board):
  return randint(0, 4)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    board[guess_row + 1][guess_col + 1] = "!"
    print_board(board)
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
      if turn >= 3:
        print("Game Over")
    else:
      print("You missed my battleship!")
      board[guess_row + 1][guess_col + 1] = "X"
      if turn >= 3:
        print("Game Over")
    print_board(board)