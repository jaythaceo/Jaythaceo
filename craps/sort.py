
# Let's do some stuff here.
# Now maybe a class is needed?
import random

def choose_word():
  words = ["Sopranos", "Tony", "Sil", "Paulie", "Artie", "Pussy", "Bada Bing"]
  return random.choice(words)

def display_words(word,guessed_letters):
  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += letter
    else:
      display += "__"
  return display

def hangman():
  word = choose_word()
  guessed_letters = []
  attempts = 6
  print("Welcome to Hangman!")

  while attempts > 0:
    print("\nWord:", display_words(word, guessed_letters))
    print("Attempts left:", attempts)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single letter.")
      continue
    if guess in guessed_letters:
      print("You already guessed that letter.")
      continue

    guessed_letters.append(guess)

    if guess not in word:
      attempts -= 1
      print("Incorrect guess.")

    if "__" not in display_words(word, guessed_letters):
      print("\nCongratulations! you guessed the word:", word)
      return
    
    print("\nYou ran out of attempts. The word was:", word)
    print("Game over!")


if __name__ == "__main__":
  hangman()