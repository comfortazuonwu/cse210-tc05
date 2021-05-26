import random
from game.word import Word
from game.player import Player


 

class Console:
    """A code template for 
    a computer console. This class of objects gets text or numerical input, displays text output and also displays the parachute.

    Stereotype:
    Service Provider

    Attributes:
    gameboard(list): The parachute 
    """

    
    def __init__(self):

       self.gameboard = ["____", "/", "\\", "____","\\" , "/","\\", "/","0","/","|","\\","/", "\\"]


    def create_parachute(self, gameboard):

        
        print(' ',self.gameboard[0])
        print (self.gameboard[1], end='')
        print('',self.gameboard[3], end='')
        print("", self.gameboard[2])
        print(self.gameboard[4], end="")
        print('    ',self.gameboard[5])
        print('',self.gameboard[6], end="")
        print('  ', self.gameboard[7])
        print('  ', self.gameboard[8])
        print('',"/","|", "\\")
        print(" ","/","\\")
        print()
        print('^^^^^^^')
                
        
       
    
    def get_text(self,prompt):
        """Gets the alphabet from the user

        Args:
        self(Screen): An instance of Screen.
        prompt(string): The prompt to display to the user
        Returns:
        string : The user's input as a string
        """
        return input(prompt)


   
        
    """ if the letter guessed is wrong, then take out something from the list"""
    def check_letter(self):
        """Checks if the letter guessed by the player is correct or not"""
        x = 0
        while x!= len(self.gameboard):
            player.get_letter()
            if get_letter in Word.letter_list:
                y = Word.letter_list.index(get_letter)
                Word.secretWord[y] = get_letter
                print(Word.secretWord)
                

                
            else:
                x +=1
                self.gameboard[x] = " "
                
    
    

            

        



    
   