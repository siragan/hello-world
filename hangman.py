import random

class hangman:

	def __init__(self, word, max_strikes = 8):
		self.word = word
		self.max_strikes = max_strikes
		self.strikes = 0
		self.guessed_letters = set()
		self.game_state = ['_']*len(self.word)

	def getword(self):
		return self.word

	def getmaxstrikes(self):
		return self.max_strikes

	def getstrikes(self):
		return self.strikes

	def getgamestate(self):
		return self.game_state

	def update(self, letter):
		for i in range(len(self.word)):
			if self.game_state[i] == '_' and self.word[i] == letter:
				self.game_state[i] = letter

	def display(self):
		for letter in self.game_state: print(letter, end = '')
		print('')
		print('strikes remaining: ' + str(self.max_strikes - self.strikes))

	def guess(self, letter):
		if len(letter) != 1:
			print('invalid input, please enter a single letter.')
		elif not letter.isalpha():
			print('invalid input, please enter a letter of the alphabet.')
		elif letter.lower() in self.guessed_letters:
			print('you have already guessed this letter, please try another one.')
		else:
			self.guessed_letters = self.guessed_letters.union({letter.lower()})
			if letter.lower() in self.word:
				for i in range(len(self.word)):
					if self.word[i] == letter.lower():
						self.game_state[i] = letter.lower()
			else:
				self.strikes += 1

if __name__ == "__main__":

	with open("vocabulary.txt") as file:
		vocabulary_list = [word for line in file for word in line.split()]

	game = hangman(random.choice(vocabulary_list))

	while (game.getstrikes() < game.getmaxstrikes()) and ('_' in game.getgamestate()):
		print('current game state:')
		game.display()
		guess = input('please guess a letter: ')
		game.guess(guess)

	if game.getstrikes() == game.getmaxstrikes():
		print('sorry, you lost! the word was: ' + game.getword())
	else:
		print('you won! the word is: ' + game.getword())