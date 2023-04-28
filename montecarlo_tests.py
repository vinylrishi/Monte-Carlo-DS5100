from montecarlo import Die
import pandas as pd
import unittest

class DieTestSuite(unittest.TestCase):
    
    def test_1_change_weight(self): 
       die1 = Die([1,2,3,4,5,6])
       die1.change_weight(3,24)
       test = 24 in die1.W
       self.assertTrue(test, 'The new weight does not exist in the data frame')
    
    def test_2_roll_results(self):
       die1 = Die([1])
       die1.roll(2)
       test = die1.roll(2)
       for t in test:
           if (t ==1):
               valid = True
           else:
               valid = False

       self.assertTrue(valid, 'Two ones should be the only possible outcome')
    
    def test_3_roll_results_false(self):
       die1 = Die([1,2])
       test = die1.roll(2)
       for t in test:
           if (t ==3):
               invalid = True
           else:
               invalid = False

       self.assertFalse(invalid, 'three is not a valid face on this die')
    
    def test_4_show(self):
       die1 = Die([1,2])
       df = die1.show()
       test = df.iloc[1,0]
       self.assertEqual(test,2) 
    


from montecarlo import Game
class GameTestSuite(unittest.TestCase):
    def test_5_play(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(4)
        df = gamer.show('narrow')
        test = df.iloc[2,0]
        self.assertEqual(test,2)

    def test_6_play_false(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(4)
        df = gamer.show('narrow')
        test = df.iloc[2,0] == 3
        self.assertFalse(test, 'Only face value possible is 2') 

    def test_7_show_nar(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(4)
        df = gamer.show('narrow')
        test = len(df.index) == 8
        self.assertTrue(test, 'There should be 8 rows (4 for each die) in the narrow df')  
    
    def test_8_show_wide(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(4)
        df = gamer.show()
        test = len(df.index) == 4
        self.assertTrue(test, 'There should be 4 rows (one for each roll) in the wide df') 



from montecarlo import Analyzer
class AnalyzerTestSuite(unittest.TestCase):
    def test_9_jackpot(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(5)
        atest = Analyzer(gamer)
        test = atest.jackpot()
        self.assertEqual(test,5)

    def test_10_face_count(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(5)
        atest = Analyzer(gamer)
        atest.face_count()
        df = atest.face_count_df
        test = df.iloc[2,0] == 2
        self.assertTrue(test, 'Bot dice should have rolled into the same face')

    def test_11_combo_count(self):
        die1 = Die([2])
        gamer = Game([die1,die1])
        gamer.play(5)
        atest = Analyzer(gamer)
        atest.combo()
        df = atest.combo_df
        test = len(df.index)
        self.assertEqual(test,1)
    
    def test_12_combo_letters(self):
        die1 = Die(['H','H'])
        gamer = Game([die1,die1])
        gamer.play(5)
        atest = Analyzer(gamer)
        atest.combo()
        df = atest.combo_df
        test = len(df.index)
        self.assertEqual(test,1)

if __name__ == '__main__':
    unittest.main(verbosity=3)