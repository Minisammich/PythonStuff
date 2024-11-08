#Jeffrey Hamilton
#October 24th, 2022 / November 17th, 2022
#Guessing Game
#CS20 P4
import random
from random import randint
from datetime import datetime
print("""
>Easy = 1-10 with 4 guesses.
>Normal = 1-30 with 8 guesses.
>Hard = 1-50 with 10 guesses.
>Extreme = 1-80 with 15 guesses.
>Impossible = 1-100 with 1 guess.

~~Alt Modes~~
>Impossible+ = -100-100 with 1 guess.
>50/50 = 1-2 with 1 guess.
>Evens = 2-100 with 4 guesses. Only Even Numbers!
>Odds = 1-99 with 4 guesses. Only Odd Numbers!
>Whack-A-Mole = 1-100, but it changes after every guess!
>Custom = You Choose!
-------------------------------------------------""")
wins = [] #Keeps track of wins
loss = [] #Keeps track of losses
previous_random_numbers = [] #Keeps track of previously generated random numbers

#Gets current time in seconds
time = datetime.now()
seconds = time.second
minutes = time.minute * 60
hours = time.hour * 3600
time_start = seconds + minutes + hours

#The main code for the game
def guessing_game():
  previous_random_numbers = []
  higher_lower = True
  changes = False
  int_range2 = 1
  difficulty = input('Easy, Normal, Hard, Extreme, Impossible, or Alternative Modes? (Default is Normal): ') #User sets difficulty
  #Checks difficulty and sets number range accordingly
  if difficulty.lower() == "easy" or difficulty.lower() == "e":
    random_number = randint(1, 10)
    num_range = "1 and 10"
    int_range = 10
    num_turns = 4
  elif difficulty.lower() == "normal" or difficulty.lower() == "n":
    random_number = randint(1, 30)
    num_range = "1 and 30"
    int_range = 30
    num_turns = 8
  elif difficulty.lower() == "hard" or difficulty.lower() == "h":
    random_number = randint(1, 50)
    num_range = "1 and 50"
    int_range = 50
    num_turns = 10
  elif difficulty.lower() == "extreme" or difficulty.lower() == "x":
    random_number = randint(1, 80)
    num_range = "1 and 80"
    int_range = 80
    num_turns = 15
  elif difficulty.lower() == "impossible" or difficulty.lower() == "i":
    random_number = randint(1, 100)
    num_range = "1 and 100"
    int_range = 100
    num_turns = 1
    higher_lower == False
  elif difficulty.lower() == "alternative" or difficulty.lower() == "a" or difficulty.lower() == "alternative modes":
    alternate_modes = input('Impossible+, 50/50, Evens, Odds, Whack-A-Mole, or Custom: ')
    if alternate_modes.lower() == "impossible+" or alternate_modes.lower() == "i+":
      random_number = randint(-100, 100)
      num_range = "-100 and 100"
      int_range = 100
      int_range2 = -100
      num_turns = 1
      higher_lower == False
    elif alternate_modes.lower() == "50/50" or alternate_modes.lower() == "5":
      random_number = randint(1, 2)
      num_range = "1 and 2"
      int_range = 2
      num_turns = 1
      higher_lower == False
    elif alternate_modes.lower() == "evens" or alternate_modes.lower() == "e":
      random_number = random.randrange(2, 102, 2)
      num_range = "2 and 100"
      int_range = 100
      int_range2 = 2
      num_turns = 4
    elif alternate_modes.lower() == "odds" or alternate_modes.lower() == "o":
      random_number = random.randrange(2, 102, 2)
      random_number = random_number - 1
      num_range = "1 and 99"
      int_range = 99
      int_range2 = 1
      num_turns = 4
    elif alternate_modes.lower() == "whack-a-mole" or alternate_modes.lower() == "w":
      random_number = randint(1, 100)
      num_range = "1 and 100"
      int_range = 100
      num_turns = int(input('How many turns?: '))
      changes = True
      higher_lower = False
    elif alternate_modes.lower() == "custom" or alternate_modes.lower() == "c":
      ir1 = int(input('Lower Limit: '))
      ir2 = int(input('Upper Limit: '))
      random_number = randint(ir1, ir2)
      num_range = ("%s and %s" % (ir1, ir2))
      int_range = int(ir2)
      int_range2 = int(ir1)
      num_turns = int(input('How many turns?: '))
      changes = input('Should the number change after each guess? (y/N): ')
      higher_lower = input('Should it tell you if the number is higher or lower? (Y/n): ')
      if changes.lower() == "y":
        changes = True
      else:
        changes = False
      if higher_lower.lower() == "n":
        higher_lower = False
      else:
        higher_lower = True
  else:
    random_number = randint(1, 30)
    num_range = "1 and 30"
    int_range = 30
    num_turns = 8
    
  #Sets/Resets the list of saved guesses
  previous_guesses = []
  
  #Runs through the guessing process to make it have multiple turns.
  turn_counter = 1
  plural = "es" #Makes "Guess%s" = "Guesses" by default, can be made blank later.
  num_wins = len(wins)
  num_losses = len(loss)
  total_games = num_wins + num_losses
  print('-----------------------------------------')
  print('Games Played = %s | Wins = %s | Losses = %s' % (total_games, num_wins, num_losses))
  print('-----------------------------------------')
  print('')
  for turn in range(1, 100):
    if changes == True:
      random_number = randint(int_range2, int_range)
      previous_random_numbers.append(random_number)
    print('( Turn', turn_counter, ")")
    user_guess = input('Guess a number between %s: ' % (num_range))
    user_guess = int(user_guess)
    ##Checks if the user has already guessed the number they just input.
    already_guessed = False
    for guess in previous_guesses:
      if user_guess == guess:
        already_guessed = True
    ##If the user has already guessed the number, it will not be counted as a turn.
    if already_guessed == True and changes == False:
      print('~~You have already guessed that number!')
      print('')
    elif user_guess < int_range2 or user_guess > int_range: #Checks if guess is valid
      print('Guess must be between %s' % (num_range))
    elif user_guess == random_number: #If correct, breaks loop.
      wins.append('x')
      previous_guesses.append(user_guess) #Adds guess to list
      print('You Win!')
      print('')
      if turn_counter == 1:
        plural = ""
      print('~You won in %s guess%s.~' % (turn_counter, plural))
      break
    else:
      previous_guesses.append(user_guess) #Adds guess to list
      print('%s is not the correct number!' % (user_guess))
      if higher_lower == True:
        if user_guess > random_number:
          print('The number is lower.')
        elif user_guess < random_number:
          print('The number is higher.')
      print('')
      turn_counter += 1
      if turn_counter == num_turns + 1:
        loss.append('x')
        print('Game Over!')
        break
        
  #Function for showing the previously guessed numbers
  def display_guesses(guess_list):
    counter = 0
    print('')
    plural2 = "were" #Makes default plural, will be changed to singular later if necessary.
    if turn_counter == 1:
      plural2 = "was"
    guesses = ""
    for guess in guess_list:
      guesses = guesses + str(guess_list[counter]) + ", "
      counter += 1
    guesses = guesses[0:len(guesses) - 2] + "."
    print('Your Guess%s %s:    %s' % (plural, plural2, guesses))
    counter = 0
    previous_random_numbers2 = ""
    if changes == False:
      print("And the number was: %s!" % (random_number))
    elif changes == True:
      previous_random_numbers2 = ""
      for item in previous_random_numbers:
        previous_random_numbers2 = previous_random_numbers2 + str(previous_random_numbers[counter]) + ", "
        counter += 1
      previous_random_numbers2 = previous_random_numbers2[0:len(previous_random_numbers2) - 2]
      print("And the numbers were: %s!" % (previous_random_numbers2))
  display_guesses(previous_guesses)
  print('')
#Runs the game, then checks if user wants to play again.
guessing_game()
while True:
  play_again = input('Play Again? (Y/n): ') #Y capitalized to show it's the default choice.
  print('--------------------------------')
  if play_again == "n": #Only quits if "n" is typed, meaning typing nothing plays it again.
    #Gets the current time and compares it to the start time to get total time played.
    time_end = datetime.now()
    sec_end = time_end.second
    min_end = time_end.minute * 60
    hour_end = time_end.hour * 3600
    time2_end = sec_end + min_end + hour_end
    time_played = time2_end - time_start
    hours_played = 0
    #Converts 60 seconds into a minute, and 60 minutes into an hour.
    if time_played >= 60:
      seconds_played = time_played % 60
      time_played = int(time_played / 60)
      minutes_played = int(time_played / 60)
      if minutes_played >= 60:
        minutes_played = minutes_played % 60
        hours_played = int(time_played / 60)
    else:
      seconds_played = time_played
      minutes_played = 0
      hours_played = 0
    print('Time played = %sh %sm %ss.' % (hours_played, minutes_played, seconds_played))
    print('')
    print('Quitting Game...')
    break
  else:
    guessing_game()