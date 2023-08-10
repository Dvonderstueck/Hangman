class Hangman:

    def __init__(self, word):
        self.word = word
        self.attempts = 7
        self.guesses = set()

    def Display_word(self):
        Display = ""
        for letter in self.word:
            if letter in self.guesses:
                Display += letter
            else:
                Display += "_"
        return Display

    def make_guess(self, letter):
        self.guesses.add(letter)
        if letter not in self.word:
            self.attempts -= 1

    def is_game_won(self):
        return set(self.word) == self.guesses

    def is_game_lost(self):
        return self.attempts == 0


def main():
    wordToGuess = "secret"
    hangman_game = Hangman(wordToGuess)

    while not hangman_game.is_game_lost() and not hangman_game.is_game_won():
        print("Word:", hangman_game.Display_word())
        guess = input("Guess a letter: ")

        if len(guess) != 1:
            print("You can only guess one letter.")
        
        hangman_game.make_guess(guess)
        print("you have", hangman_game.attempts, "left")


        if hangman_game.is_game_won():
          print("Congratulations! You won the game.")
        else:
         print("Sorry, you lost. The word was:", wordToGuess)
    


if __name__ == "__main__":
    main()
