class Player:
    """A code template for the player who guesses a letter. The responsibility 
    of this class of objects is to get the users input about which letter they
    would like to guess and return that letter.

    Stereotype:
        Information Holder

    Attributes:
        letter (string): The prompt to display on each line.
    """

    def get_letter(self, letter):
        """Gets and returns the letter the player guesses.

        Args: 
            self (Player): An instance of Player.
            letter (string): The prompt to display to the user.

        Returns:
            string: The user's input as text (one letter).
        """
        letter = input("Guess a letter [a-z]: ")
        return letter