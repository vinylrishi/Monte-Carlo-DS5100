import pandas as pd
import numpy as np
class Die():
    """
    Creates a Die object with N sides and W weights

    Initialized:

        N: An array of faces (as strings or numbers) entered by user
        W: Weights of each face that defaults to 1.0 for each. Can be changed later by user.
        _df: A private data frame that holds each face and the coresponding weight

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
    
    # Initializer
    def __init__(self, N):
        self.N = N
        self.W = np.ones(len(N), dtype=float)
        self._df = pd.DataFrame({'Faces':self.N, 'Weights':self.W})  
    
    def change_weight(self,F, w):
        if(F in self.N):
            try:
                self._df.loc[self._df.Faces == F, 'Weights'] = float(w)
                self.W[self._df.Faces == F] = float(w)
            except:
                print("The weight entered is not a valid number")
        else:
            print('The value entered is not a face on the object')

    def roll(self, r=1):
        sumw = sum(self._df['Weights'])
        outcomes = np.random.choice(self.N,r,p=self._df['Weights']/sumw)
        return outcomes.tolist()
    
    def show(self):
        return self._df



class Game():
    """
    A game is played by rolling one or more Die objects if the same kind, meaning they have the same faces. The weights of the Die objects can differ.

    Initialized: 

        dice: a list of similar Die objects that have already been instantiated by the user.
        _game: empty data frame that will be populated via the play method

    Methods:

    play(rolls): 

        Rolls each die in dice list the inputed number of times

        rolls: number of desired rolls per die 

        Saves a private data frame (self._game) with results of the rolls for each die

    show(shape): 
    
        Returns a data frame of the latest game's results to the user
        
        shape: the desired shape of the returned data frame (narrow or wide). Default is wide.

        Make sure the game has been played before trying to get the data frame!
    
    """
    # Initializer
    def __init__(self, dice):
        self.dice = dice
        self._game = pd.DataFrame(columns=['Die Number', 'Face Rolled'])

    def play(self, rolls = 1):
        for i in range(0,len(self.dice)):
            die_n = [i]*rolls
            results = self.dice[i].roll(rolls)
            tempdf = pd.DataFrame({'Die Number': die_n, 'Face Rolled': results})
            self._game = pd.concat([self._game,tempdf], axis = 0)
        
        self._game.index.name = 'Roll Number'
        self._game.index+=1
    
    def show(self, shape = 'wide'):
        if(shape == 'wide'):
            try:
                df = self._game.pivot_table(index = 'Roll Number', columns='Die Number', values='Face Rolled', aggfunc = lambda x: x)
                return df
            except:
                raise Exception('Make sure you have played the game!')
        elif(shape == 'narrow'):
            try:
                df = self._game.copy()
                df = df.reset_index()
                df.set_index(['Roll Number','Die Number'], inplace=True)
                return df
            except:
                raise Exception('Make sure you have played the game!')
        else:
            raise Exception('Must enter narrow or wide as options for data frame. Also, make sure you have played the game!')
        



class Analyzer():
    """
    Takes result of Game object and computes different satistics around outcomes using various methods (listed below)
    
    Initialized: 
        game: Game object passed in by user
        _game_df = private copy of narrow data frame from game results that has reset indices. Allows for easier manipulation and grouping.
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
    # Initializer
    
    def __init__(self, game):
        self.game = game
        self._game_df = self.game.show('narrow').copy().reset_index()
        self.jackpot_df = pd.DataFrame()
        self.combo_df = pd.DataFrame()
        self.face_count_df = pd.DataFrame()
        die1 = game.dice[0].show()
        self.face_type = type(die1.iloc[:,0][0])
    
    def face_count(self): 
        fcdf = self._game_df.groupby(['Roll Number','Face Rolled']).size()
        fcdf = fcdf.to_frame('Face Counts')
        fcdf = fcdf.reset_index()
        self.face_count_df = fcdf.pivot_table(index = 'Roll Number', columns='Face Rolled', values='Face Counts', fill_value = 0)
    
    def jackpot(self):
        jpdf = self._game_df.groupby(['Roll Number','Face Rolled']).size()
        jpdf = jpdf.to_frame('Face Counts')
        jpdf = jpdf.reset_index()
        jpdf = jpdf.pivot_table(index = 'Roll Number', columns='Face Rolled', values='Face Counts', fill_value = 0)
        die_count = len(self.game.dice)
        self.jackpot_df = jpdf[jpdf.max(axis=1) == die_count]
        jackpot_count = len(self.jackpot_df.index)
        return jackpot_count
    
    def combo(self): 
        cdf =  self._game_df.groupby(['Roll Number','Face Rolled','Die Number']).size()
        cdf = cdf.to_frame('Count')
        cdf = cdf.reset_index()
        cdf = cdf.pivot_table(index = 'Roll Number', columns='Die Number', values='Face Rolled', aggfunc = lambda x: x)
        cdf = cdf.apply(lambda x: sorted(x), axis=1, result_type='expand')
        self.combo_df = cdf.value_counts().to_frame('Frequency')
        
    
