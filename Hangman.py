num_of_tries = 1


def main():

    def print_opening_art():
        HANGMAN_ASCII_ART = ("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
    """)
        MAX_TRIES = 6
        return print(HANGMAN_ASCII_ART, MAX_TRIES)
    print_opening_art()
    """
    Prints the opening ASCII art and the maximal number of tries given in this game.
    :param HANGMAN_ASCII_ART: The opening ASCII art, const
    :param MAX_TRIES: Maximal number of tries given in hangman game, const
    :type HANGMAN_ASCII_ART: str
    :type MAX_TRIES: str
    :return: Opening ASCII art and Maximal number of tries printed
    :rtype: str
    """

    def choose_word(file_path, index):
        words_file = open(file_path, "r")
        words_string = words_file.read()
        split_words_list = words_string.split()
        unique_words = set(split_words_list)
        unique_words_list = list(unique_words)
        unique_words_count = len(unique_words_list)
        real_index = (index % unique_words_count) - 1
        words_file.close()
        return unique_words_list[real_index]

    """
    Chooses the word to be guessed out of an existing txt file.
    :param word_file: The creation of a reading only file
    :param words_string: Reading the file content and turning it into a string
    :param split_words_list: Splits the string into a list of individual words
    :param unique_words: Creates a set of the words without their repetitions.
    :param unique_words_list: Returns to list type, with only one repetition of each word.
    :param real_index: Remnant of index when total of unique words divided by it (mod) minus 1 for real py index

    :type word_file: str
    :type words_string: str
    :type split_words_list: list
    :type unique_words: set
    :type unique_words_list: list
    :type real_index: int
    :return: word in the specific index entered from the str in the file
    :rtype: str
    """

    your_file_path = input("Enter file path: ")
    your_index = int(input("Enter a number: "))
    # C:\Users\97252\New folder\words.txt on Xanders computer
    secret_word = choose_word(your_file_path, your_index)
    old_letters_guessed = []
    print("_ " * len(str(secret_word)))

    def check_valid_input(letter_guessed, old_letters_guessed):
        one_letter = bool(0 < int(len(letter_guessed)) < 2)
        not_symbol = bool(letter_guessed.islower())
        if (one_letter and not_symbol) and (letter_guessed not in old_letters_guessed):
            return bool(True)
        else:
            return bool(False)

    """
    Checks that the input is a single letter, not already guessed, and not a symbol or longer str
    :param one_letter: The truth value of the length of the str guessed being smaller than 2 and larger than 1
    :param not_symbol: Truth value of the note guessed being possible to lowkey - a letter.
    :type one_letter: boolean
    :type not_symbol: boolean
    :return: Boolean value true if letter not guessed and is a single letter only. False else.
    :rtype: boolean
    """

    def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        global num_of_tries
        old_letters_guessed_list = sorted(old_letters_guessed)
        with_arrows = ' -> '.join(old_letters_guessed_list)
        if check_valid_input(letter_guessed, old_letters_guessed):
            old_letters_guessed.append(letter_guessed)
            print("valid")
            if letter_guessed not in secret_word:
                num_of_tries += 1
                print("Wrong.")
                print(with_arrows)
                return num_of_tries
            else:
                print("Right!")
                return num_of_tries
        else:
            old_letters_guessed.append(letter_guessed)
            num_of_tries += 1
            if len(letter_guessed) > 1 and letter_guessed.isalpha():
                print("not a single letter!")
                print(with_arrows)
                return num_of_tries
            elif not letter_guessed.isalpha():
                print("Not a letter!")
                print(with_arrows)
                return num_of_tries

    """
    Updates letters that were already guessed as a list joined with " -> ".
    :param old_letters_guessed_list: a list of the words in old_letters_guessed, in order to sort them
    :param with_arrows: a string connecting the letters in old_letters_guessed_list using " -> "
    :type old_letters_guessed_list: list
    :type with_arrows: str
    :return: number of tries done
    :rtype: int
    """

    def print_hangman(num_of_tries):
        HANGMAN_PHOTOS = {'1': """
            x-------x
            """, '2': """
                x-------x
                |
                |
                |
                |
                |
            """, '3': """
                x-------x
                |       |
                |       0
                |
                |
                |
            """, '4': """
                x-------x
                |       |
                |       0
                |       |
                |
                |
            """, '5': """
                x-------x
                |       |
                |       0
                |      /|\\
                |
                |
            """, '6': """
                x-------x
                |       |
                |       0
                |      /|\\
                |      /
                |
            """, '7': """
                x-------x
                |       |
                |       0
                |      /|\\
                |      / \\
                |
            """}
        for key in HANGMAN_PHOTOS.keys():
            key = str(num_of_tries)
            return print(HANGMAN_PHOTOS[key])
    """
    prints the feedback to the user by drawing a hangman depends on his number of failures.
    :param HANGMAN_PHOTOS: A dict of the different drawings of the hangman by the key of num_of_tries, const.
    :param num_of_tries: The number of tries done by the user
    :type HANGMAN_PHOTOS: dict
    :type num_of_tries: int, turns into str
    :return: Printing a hangman photo from the dict, using the num_of_tries as key
    :rtype: str
    """

    def show_hidden_word(secret_word, old_letters_guessed):
        output_word = ""
        for letter in secret_word:
            if letter in old_letters_guessed:
                output_word += letter
            else:
                output_word += " _ "
        return output_word, num_of_tries

    """
    shows how much of the word was discovered by user.
    :param output_word: a string of the secret word with only the rightly guessed letters exposed
    :param secret_word: the word to be guessed, as shown previously in the code
    :param old_letters_guessed: a list of the letters that were guessed by user, as shown previously in code
    :type output_word: str
    :type secret_word: str
    :type old_letters_guessed: list
    :return: a string of the secret word with only the rightly guessed letters exposed, number of tries
    :rtype: tuple
    """

    def check_win(secret_word, old_letters_guessed):
        secret_as_list = list(secret_word)
        for letter in secret_as_list:
            if letter in old_letters_guessed:
                win_value = True
            else:
                win_value = False
            return win_value

    """
    shows whether the user won or lost the hangman games.
    :param secret_as_list: secret_word shown as a list of letters
    :param old_letters_guessed: a list of the letters that were guessed by user, as shown previously in code 
    :type secret_as_list: list
    :type old_letters_guessed: list
    :return: a boolean value of the winning status 
    :rtype: boolean
    """
    while int(num_of_tries) < 7:
        letter_guessed = input("Guess a letter: ")
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed))
        print_hangman(num_of_tries)

    if num_of_tries == 7:
        print("Game Over. Are you winning son?")
        print(check_win(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()
