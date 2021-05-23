import random


 

class Console:
    """A code template for 
    a computer console. This class of objects gets text or numerical input, displays text output and also displays the parachute.

    Stereotype:
    Service Provider

    Attributes:
    gameboard(list): The parachute 
    """

    
    def __init__(self):

       gameboard = ["____", "/", "\\", "____","\\" , "/","\\", "/","0","/","|","\\","/", "\\"]


    def create_parachute(self, gameboard):

        
        print(' ',gameboard[0])
        print (gameboard[1], end='')
        print('',gameboard[3], end='')
        print("", gameboard[2])
        print(gameboard[4], end="")
        print('    ',gameboard[5])
        print('',gameboard[6], end="")
        print('  ', gameboard[7])
        print('  ', gameboard[8])
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


    def write(self,text):

        print(text)
        
""" if the letter guessed is wrong, then take out something from the list"""
