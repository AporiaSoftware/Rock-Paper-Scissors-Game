#Imports random function to allow computer to pick random choice
import random

#Asks if you want to play a game and outlines a broad if/else statement defining the game
game_start = input("'Would you like to play a game?' : [Y/N]\n")
if game_start == "y" or game_start == "Y":
  #Provides a function to launch rock, paper, scissors
  def game():
    #True/False and while statement to provide the beginning of a loop
    rps = True 
    while rps:
      #Action phase of the game
      print("\n'Quick! Rock, Paper, Scissors, Shoot!'")
      user_choice = input("Enter a choice: ")
      possible_choices = ["rock", "paper", "scissors"]
      computer_choice = random.choice(possible_choices)
      print(f"\nYou picked {user_choice}, the computer picked {computer_choice}.\n")
      #Decides winner/loser/tie and outputs the outcome, asks to play again
      if user_choice.lower() == computer_choice:
        print(f"'Both players picked {user_choice}. It's a draw.'")
      elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
          print("'Rock breaks scissors! Aw man, you win!'")
        else:
          print("'Paper covers rock! Sucks for you, loser!'")
      elif user_choice.lower() == "paper":
        if computer_choice == "rock":
          print("'Paper covers rock! You win!'")
        else:
          print("'Scissors cuts paper! Better luck next time.'")
      elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
          print("'Scissors cuts paper! You won this one..'")
        else:
          print("'Rock smashes scissors! You lose this time.'")
      x = input("'Play again?' Y or N?\n") 
      if x == "y" or x == "Y":
        #Loops game function
        game()
      else:
        #Ends game
        print("\n'Let's play again some time!'") 
        rps = False
      #Breaks loop after game end
      break
  game()
#breaks if/else statement if user does not want to play a game
else:
  print("\n'Another time maybe.'")
