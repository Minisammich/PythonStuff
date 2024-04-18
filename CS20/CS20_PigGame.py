import random

def dice(x): #A virtual 6 sided die
  output = 0
  for i in range(x):
    output += random.randint(1,6)
  return(output)

### Milestone 1: Computer (Singleplayer)
def milestone1():
  score = 0 #Total score
  turn_total = 0 #Total of rolls per turn
  turn_count = 1 #Turn Counter
  has_won = False #Whether win condition has been reached or not
  print_turn = True #Whether to print turn count or not
  while has_won == False: #Main loop for the game. Repeats as long as you haven't won.
    roll = dice(1) #Stores the roll of a die (1-6)
    if print_turn == True and turn_total <= 20 and score < 100: #Prints the turn count.
      print('''
      Turn: %s''' % (turn_count))
    if score >= 100: #If score limit is reached it prints victory message.
      turn_count -= 1 #Removes the extra turn it adds when it loops after it already won
      print('''
You Won in %s Turns with a score of %s!''' % (turn_count, score))
      has_won = True #Ends loop by setting has_won to True
    elif turn_total >= 20: #If turn total limit reached, increments turn and adds turn total to score.
      print_turn = True #print_turn makes the turn count get printed at start of loop if set to True
      turn_count += 1
      score += turn_total
      turn_total = 0
      print('''Score: %s''' % (score)) #Prints out score
    else:
      if roll != 1: #If roll isn't 1,
        print_turn = False #DOESN'T print turn count at start of loop
        turn_total += roll #Adds roll to turn_total
        print('''Roll: %s
Turn Total: %s''' % (roll, turn_total)) #Prints roll and new turn total
      else: #If roll IS 1,
        print_turn = True #Ensures turn is printed
        turn_count += 1 #Increments turn
        turn_total = 0 #Resets turn total without adding to score first.
        print('''Roll: 1
Turn Total: 0
Score: %s''' % (score))

### Milestone 2: Computer vs Computer
def milestone2():
  player1_score = 0
  player1_turn_total = 0
  player1_turns = 1
  player1_has_won = False
  player1_print_turn = True
  player2_score = 0
  player2_turn_total = 0
  player2_turns = 1
  player2_has_won = False
  player2_print_turn = True
  turn = random.randint(0,1) #Randomizes starting player.
  while player1_has_won == False and player2_has_won == False: #Loops until either wins
    roll = dice(1)
    if player1_score >= 100: #If player1's score is 100 or over, they win.
      player1_has_won = True
      player1_turns -= 2
      print('''
Player 1 has won in %s turns with a score of %s!''' % (player1_turns, player1_score))
    elif player2_score >= 100: #If player2's score is 100 or over, they win.
      player2_has_won = True
      print('''
Player 2 has won in %s turns with a score of %s!''' % (player2_turns, player2_score))
      
    elif turn % 2 == 0: #If turn is even, player1 goes.
      if player1_print_turn == True and player1_score < 100 and player1_turn_total < 20: #Checks if players turn shold be printed and they haven't already won, then prints the turn.
        print('''
        Player 1's Turn: %s''' % (player1_turns))
        player1_print_turn = False
        player2_print_turn = True #Sets opposing player's print_turn to True.
      if player1_turn_total >= 20: #If player1 reaches it's turn limit,
        turn += 1 #Increments turn
        player1_print_turn = True #player1's print_turn to True
        player1_score += player1_turn_total #Adds player1's turn_total to their score
        player1_turns += 1 #Increments player1's turn
        player1_turn_total = 0 #Resets their turn total
        print('Score: ', player1_score)
      else:
        if roll != 1: #If roll is anything other than 1,
          player1_print_turn = False #does not print turn
          player1_turn_total += roll #Adds roll to their turn_total
          print('''Roll: %s
Turn Total: %s''' % (roll, player1_turn_total))
        else: #If roll is 1,
          turn += 1 #Increments turn
          player1_print_turn = True #does print player1's turns
          player1_turns += 1 #Increments their turns
          player1_turn_total = 0 #Resets turn total without adding it to score first
          print('''Roll: 1
Turn Total: 0
Score: %s''' % (player1_score))
  
    elif turn % 2 != 0: #If turn is odd, player2 goes.
      if player2_print_turn == True and player2_score < 100 and player2_turn_total < 20: #Checks if players turn shold be printed and they haven't already won, then prints the turn.
        print('''
        Player 2's Turn: %s''' % (player2_turns))
        player2_print_turn = False
        player1_print_turn = True #Sets opposing player's print_turn to True.
      if player2_turn_total >= 20: #If player2 reaches it's turn limit,
        turn += 1 #increment turn
        player2_print_turn = True #print their turns = True
        player2_score += player2_turn_total #Adds their turn total to their score
        player2_turns += 1 #Increments their turn counter
        player2_turn_total = 0 #Resets their turn_total
        print('Score: ', player2_score)
      else:
        if roll != 1: #If roll is anything other than 1
          player2_print_turn = False #Does NOT print turn
          player2_turn_total += roll #Adds roll to their score
          print('''Roll: %s
Turn Total: %s''' % (roll, player2_turn_total))
        else: #If roll IS 1,
          turn += 1 #Increment turn
          player2_print_turn = True #Sets their print_turn to True
          player2_turns += 1 #Increments their turn
          player2_turn_total = 0 #Resets their turn_total without first adding it to score
          print('''Roll: %s
Turn Total: %s
Score: %s''' % (roll, player2_turn_total, player2_score))
  

### Milestone 3: Player vs Computer
def milestone3():
  player_score = 0 #Player's total score
  player_turn_total = 0 #Player's total per turn
  player_turns = 1 #Player's turn count
  player_has_won = False #Whether player has won or not
  player_print_turn = True #Whether to print player's turn count or not
  
  computer_score = 0 #Computer's total score
  computer_turn_total = 0 #Computer's total per turn
  computer_turns = 1 #Computer's turn count
  computer_has_won = False #Whether computer has won or not
  computer_print_turn = True #Whether to print computer's turn count or not
  comp_lim = 19 #Sets the turn total the computer will stop rolling at.
  
  turn = random.randint(0,1) #Makes first player randomized for fairness.
  
  while player_has_won == False and computer_has_won == False: #Loops until either win
    roll = dice(1)
    if player_score >= 100: #If player's score is 100 or greater, they win.
      player_has_won = True
      player_turns -= 2
      print('''
Player has won in %s turns with a score of %s!''' % (player_turns, player_score))
    elif computer_score >= 100: #If computer's score is 100 or greater, they win.
      computer_has_won = True
      print('''
Computer has won in %s turns with a score of %s!''' % (computer_turns, computer_score))
      
    elif turn % 2 == 0: #Player goes on even turns
      if player_print_turn == True and player_score < 100 and player_turn_total < 20:
        print('''
        Player's Turn: %s''' % (player_turns))
        player_print_turn = False
        computer_print_turn = True
      elif (input('Do you want to roll? (Y/n): ')).lower() == "n":
        if player_score + player_turn_total >= 100:
          player_turns += 1
        else:
          turn += 1
        player_score += player_turn_total
        player_turn_total = 0
        player_turns += 1
        print('''Score: %s''' % (player_score))
        player_print_turn = True
      else:
        if roll != 1:
          player_print_turn = False
          player_turn_total += roll
          print('''Roll: %s
Turn Total: %s''' % (roll, player_turn_total))
        else:
          turn += 1
          player_print_turn = True
          player_turns += 1
          player_turn_total = 0
          print('''Roll: 1
Turn Total: 0
Score: %s''' % (player_score))
  
    elif turn % 2 != 0: #Computer goes on odd turns
      if computer_print_turn == True and computer_score < 100 and computer_turn_total < comp_lim:
        print('''
        Computer's Turn: %s''' % (computer_turns))
        computer_print_turn = False
        player_print_turn = True
      if computer_turn_total >= comp_lim:
        turn += 1
        computer_print_turn = False
        computer_score += computer_turn_total
        computer_turns += 1
        computer_turn_total = 0
        print('Score: ', computer_score)
      elif roll != 1:
        computer_print_turn = False
        computer_turn_total += roll
        print('''Roll: %s
Turn Total: %s''' % (roll, computer_turn_total))
      else:
        turn += 1
        computer_print_turn = True
        computer_turns += 1
        computer_turn_total = 0
        print('''Roll: 1
Turn Total: 0
Score: %s''' % (computer_score))


### Milestone Selector:
playagain = True
while playagain == True:
  userinput = input('''
  Milestone 1, 2, or 3?: ''')
  if userinput == '1':
    milestone1()
  elif userinput == '2':
    milestone2()
  elif userinput == '3':
    milestone3()
  else:
    print('Type "1", "2", or "3"')
  userinput2 = input('''
  Play again? (Y/n): ''')
  if userinput2.lower() == "n":
    playagain = False