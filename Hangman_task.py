import random

hangman_graphics = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    '''
]

#Võtab minu listist suvalise sõna
def get_random_word(words):
    return random.choice(words)

#Funktsioon võtab sõna ja arvatud tähtede arvu, et returnida sõna stringi esitluse
#Iga arvatud täht sõnas (kui see on õigesti arvatud) kuvatakse
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

#Näitab, mitu elu on alles (kasutab hangman graphics listi)
def display_hangman(lives_left):
    print(hangman_graphics[6 - lives_left])

#Funktsioon, mis paneb mängu käima
def play_game():
    try:
        with open("countries-and-capitals.txt") as file:
            guessable_words = [line.split(" | ")[0].strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: 'countries-and-capitals.txt' not found. Make sure the file is in the same directory.")
        return
    
    print("Welcome to Hangman -- Guessing Game")
    print("difficulty levels:")
    print("\t1. Beginner (6 lives)") #\t teeb tabi
    print("\t2. Intermediate (5 lives)")
    print("\t3. Advance (4 lives)")

    while True:
        difficulty = input("Please select a difficulty level by typing a number 1, 2 or 3: ").strip()
        if difficulty not in {"1", "2", "3"}:
            print("Invalid choice. Please select 1, 2, or 3.")
        else:
            difficulty = int(difficulty)
        break

    word = get_random_word(guessable_words)
    guessed_letters = []
    wrong_guesses = []
    #lives parameter (at least between 3 and 7) - See tähendab, et 4, 5 või 6
    lives = 7 - difficulty
    used_letters = set()

    print(f"The word has {len(word)} letters")

    #Põhiloop, mis jookseb, kuni mängija sureb
    while lives > 0:
        print("\nCurrent word " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        display_hangman(lives)

          #Mängija arvab
        guess = input("Enter a letter (or type quit to exit): ").lower()

          #Annab võimaluse mängu lõpetada
        if guess == 'quit':
            print("Goodbye!")
            break
        
        #Kui täht on juba arvatud, siis me informeerime mängijat sellest.
        if guess in used_letters:
            print(f"You have already guessed {guess}. Try again")
            continue

        #Kui täht pole üksik täht tähtestikust või tühik, siis palutakse uuesti proovida

        if len(guess) != 1: #peab olema ainult 1 tähemärk
            print("Please enter a single letter.")
            continue
        #pikkust pole vaja enam kontrollida
        if not guess.isalpha() and not guess.isspace():
            print("Please enter an alphabetic character or space.")
            continue

        used_letters.add(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations, you've guessed the word: {word}!")
            break

        if lives == 0:
            print(f"\nSorry, you lost! The word was: {word}")
            display_hangman(lives)
            break

        #Lisame juba arvatud tähe arvatud tähtede nimekirja
        used_letters.add(guess)
        
        #Kui täht on õigesti arvatud, näidatakse hetketulemust
        if guess in word.lower():  # Case-insensitive comparison by converting both word and guess to lowercase
            # We update the guessed letters list to reveal all instances of the guessed letter in the word
            guessed_letters.extend([letter if letter.lower() == guess else '_' for letter in word])
            guessed_letters = list(dict.fromkeys(guessed_letters))  # Remove duplicate letters from guessed_letters
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            # If the guess is incorrect, we add it to the list of wrong guesses and reduce the number of lives
            wrong_guesses.append(guess)
            lives -= 1  # Reduce a life for each incorrect guess
            print(f"Oops! The letter '{guess}' is not in the word.")

        #Kontrollib, kas mängija on võitnud
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations, you've guessed the word: {word}!")
            break

        #Kontrollib, kas mängija on kaotanud (elud on otsas)
        if lives == 0:
            print(f"\nSorry, you lost! The word was: {word}")
            display_hangman(lives)  # Display the final hangman state when the player loses
            break

play_game()