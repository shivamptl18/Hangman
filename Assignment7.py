import random
def hangman():
    print('*****************************************************')
    print('               Welcome to hangman!')
    print('  I have selected a word from an english dictionary.')
    print('  I will first show you the length of the secret word')
    print('  as a series of dashes')
    print('  Your task is to guess the secret word one letter at a time.')
    print('  if you guess a correct letter, I will show you the guessed')
    print('  letter(s) in the correct position')
    print('  You can only make 8 wrong guesses before you are hung')
    print('                 Good Luck')
    print('*****************************************************')
    infile = open('dictionary.txt', 'r') ##reading the text file
    reader = infile.read()
    x = reader.split('\n')
    infile.close()
    word = x[int(random.randrange(0, len(x)-1))] ##using random function
    guesser = []
    for i in word:
        guesser.append('-')
    s = ''
    for j in guesser:
        s += j
    print(s)
    guess = 8
    while(guess != 0):
        s = ''
        guessedLetter = input('Enter a letter you want to guess: ') ##asking the user to enter a letter
        if guessedLetter in word:
            for i in range(len(word)):
                if word[i] == guessedLetter:
                    guesser[i] = guessedLetter
        else:
            guess -= 1
            print('Incorrect guess! ' + str(guess) + ' guesses remaining') ##guessed incorrectly and showing number of guesses remaining
        for j in guesser:
            s += j
        print(s)
        counter = 0
        for i in guesser:
            if i == '-':
                counter += 1
        if counter == 0:
            print('You have won! The word was ' + word + ' Thank you for playing!')
            break
    if guess == 0:
        print('You have lost! The word was ' + word + ' better luck next time!')       

        playAgain = input('Do you want to play again? Please enter(y/n) ') ##asking the user if he/she wants to play again y/n
        if playAgain == 'y':
            hangman()
        if playAgain == 'n':
                print('Okay. See you next time!')


hangman()
    
