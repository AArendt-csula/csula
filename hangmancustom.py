#Amy Arendt Custom Hangman

import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Movies':'gladiator titanic wicked split highlander nosferatu longlegs psycho splash'.split(),
'Flowers':'petunia rose lavender chrysanthemum lilac daisy amaryllis aster carnation sunflower orchid dahlia'.split(),
'Big Cats':'panther lion tiger leopard cougar jaguar cheetah puma'.split(),
'Pizza Toppings':'pepperoni mushroom pineapple peppers onions sausage chicken bacon spinach cheese ham olives sardines banana'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord, score):
    print(HANGMAN_PICS[len(missedLetters)])
    print(f"\nScore: {score}") # adding score board with f-string formatting
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
        
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# game start
print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

totalScore = 0 #track total score across games


while True:
    missedLetters = ''
    correctLetters = ''
    score = 0 #reset score for each round
    secretWord, secretSet = getRandomWord(words)
    gameIsDone = False


    
    print('The secret word is in the set: ' + secretSet)

    while not gameIsDone:
        displayBoard(missedLetters, correctLetters, secretWord, totalScore + score)
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess
            score += 10 #points for correct guess

            if all (letter in correctLetters for letter in secretWord):
                score += 50 #bonus points for completing word
                totalScore += score
                print(f'You guessed the secret word! The word was {secretWord}. You won!')
                print(f'Current Total Score: {totalScore}')
                gameIsDone = True
              

        else:
            missedLetters += guess
            score -= 5 #lose points for wrong guess

        
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord, totalScore)
                print(f'RIP. You ran out of guesses! The word was "{secretWord}".')
                print(f'Your score for this round: {score}')
                totalScore += score
                gameIsDone = True

    if not playAgain():
        print(f'Final Total Score: {totalScore}')
        print("Thanks for playing! Press Enter to exit.")
        input()
        break

    
