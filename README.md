# Monte-Carlo-DS5100

# Meta Data  
Rishi Sharma  
DS5100 Spring 2023  
Monte Carlo Simulator  

# Synopsis  
This repo contains files that create and demonstrate a simple Monte Carlo Simulator  
Installing the classes from within a shared folder of the package is simple:  

"!pip install -e ." if the montecarlo.py file is the only one in the directory and you wish to install.  

Otherwise, use "pip install" with the specifide location of the package in the directory.  

To import the entire module, use something like "import montecarlo as mc" in your notebook or py file.  
To import specific classes, use "from montecarlo import Analyzer", where Analyzer can be subtituted by Die or Game, depending on the class desired.  

# Sample Code

Sample code for creating dice:  

diefair = mc.Die([1,2,3,4,5,6])  
dietype1 = mc.Die([1,2,3,4,5,6])  
dietype2 = mc.Die([1,2,3,4,5,6])  

dietype1.change_weight(6,5)  
dietype2.change_weight(1,5)  

Here, we created 1 fair die and 2 unfair die.   


Sample code for playing a Game with Die objects:  

fair_d_game = Game([diefair,diefair,diefair,diefair,diefair])  
fair_d_game.play(100)

This will run a simulation for rolling five fair dice 100 times each.  

Sample code for Analyzing games:  

analyzing = Analyzer(fair_d_game)  
jackpots = analyzing.jackpot()

This will return the number of jackpots (all mathcing faces) in the game played. There are also methods for storing all combinations found, as well as the face counts of the Game within the Analyzer class.  


# API Description  

 class Die(N):   
  """ 
   Creates a Die object with N sides and W weights

    Initialized:

        N: An array of faces (as strings or numbers) entered by user
        W: Weights of each face that defaults to 1.0 for each. Can be changed later by user.
      
    Methods:

    change_weight(F,w): 
        
        This method allows the user to change the weight of a face
        
        F: Face to be changed (must be one that is in object)
        w: The desired weight of the face (input as a float)

        nothing is returned, but the data frame is altered

    
    
    roll(r): 
        
        Obtains a random sample of n rolls based on the weights of the die

        r: parameter for how many times to roll the die (defaults to 1)

        returns a list of outcomes from each roll

    
    show(): 
       
        Returns the current data frame with faces and weights being used in die
    
    """
    
    
    class Game(dice):
    """
    A game is played by rolling one or more Die objects if the same kind, meaning they have the same faces. The weights of the Die objects can differ.

    Initialized: 

        dice: a list of similar Die objects that have already been instantiated by the user.

    Methods:

    play(rolls): 

        Rolls each die in dice list the inputed number of times

        rolls: number of desired rolls per die 

        Saves results of the rolls for each die

    show(shape): 
    
        Returns a data frame of the latest game's results to the user
        
        shape: the desired shape of the returned data frame (narrow or wide). Default is wide.

        Make sure the game has been played before trying to get the data frame!
    
    """  
    
    class Analyzer(game):
    """
    Takes result of Game object and computes different satistics around outcomes using various methods (listed below)
    
    Initialized: 
        game: Game object passed in by user
        jackpots: empty dataframe that will be populated by jackpot method
        combos: empty dataframe that will be populated by combo method
        face_counts: empty dataframe that will be populated by face_counts method
        die1: sample die from game to help determine the data type of faces
        face_type: utilizes die1 to determine data type of faces on die
   

    Methods:

    face_count(): 
    
        Computes how many times each face is rolled in each roll. 
    
        Saves counts in self.face_counts.

    jackpot(): 

        Creates data frame of each roll that resulted in all die having the same face.
        Saves results in self.jackpot_df


        Returns count of rolls with all same faces to user.


    combo(): 

     Method to compute the distinct combinations of faces rolled, along with their counts.

     Stores results in self.combo_df data frame.        

    
    """
    
    
# Manifest  

.gitignore
FinalProjectSubmission.ipynb
LICENSE
README.md
letter_weights.txt
montecarlo-test-results.txt
montecarlo/__init__.py
montecarlo/montecarlo.py
montecarlo_demo.ipynb
montecarlo_tests.py
setup.py
    
    
