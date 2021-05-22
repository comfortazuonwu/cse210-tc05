import random

class Console:
    """A code template for 
    a computer console. This class of objects gets text or numerical input, displays text output and also displays the parachute.

    Stereotype:
    Service Provider

    Attributes:
    gameboard(list): The parachute 
    """


    def game_list(self):

       gameboard:["___","/ \","___","\ /","\ /","0",]


    def create_parachute(self):

       
         _____
        /_____\
        \     /
         \   /
           0
         / | \
        /     \ 
       
    
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
        
