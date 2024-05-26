Number Guessing Game in Python:
This Python script implements a fun and engaging guessing game. You'll be challenged to guess a hidden number between 1 and 200 in six tries or less!


Features:
*Interactive Gameplay: The script guides you through the game with clear instructions and feedback.
*User-Friendly Interface: Enter your name for a personalized experience.
*Input Validation: Ensures you enter valid numbers within the specified range.
*Informative Messages: Provides hints to help you get closer to the hidden number.
*Replayability: Easily restart the game and test your guessing skills again.


How to Play:
*Save the script as guessing_game.py.
*Run the script from your terminal using python guessing_game.py.
*Follow the on-screen prompts to enter your name and start guessing!


  
import random
import time

def get_name():
  """Asks the user for their name and returns it."""
  print("May I ask you for your name?")
  return input()

def intro(name):
  """Greets the user and explains the game."""
  print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
  time.sleep(0.5)
  print("Go ahead. Guess!")

def pick():
  """Runs the guessing game logic."""
  number = random.randint(1, 200)  # Pick a random number
  guesses_taken = 0

  while guesses_taken < 6:
    time.sleep(0.25)
    guess_str = input("Guess: ")

    try:
      guess = int(guess_str)

      if 1 <= guess <= 200:  # Validate guess range
        guesses_taken += 1

        if guesses_taken < 6:
          if guess < number:
            print("Your guess is too low.")
          elif guess > number:
            print("Your guess is too high.")
          else:  # Correct guess
            break
          print("Try again!")
      else:
        print("Silly Goose! That number isn't in the range (1-200)!")
    except ValueError:
      print(f"I don't think '{guess_str}' is a number. Sorry!")

  if guess == number:
    guesses_taken_str = str(guesses_taken)
    print(f'Good job, {name}! You guessed my number in {guesses_taken_str} guesses!')
  else:
    print(f'Nope. The number I was thinking of was {number}')

def main():
  """Runs the game loop."""
  play_again = "yes"
  while play_again.lower() in ("yes", "y"):
    name = get_name()
    intro(name)
    pick()
    print("Do you want to play again?")
    play_again = input()

if __name__ == "__main__":
  main()
