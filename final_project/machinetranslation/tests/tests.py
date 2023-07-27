import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french('Hello') ,'Bonjour')

    def test_english_to_french_good_morning(self):
        self.assertEqual(english_to_french('Good morning!') ,"J'espère que vous allez bien !")
    
    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english('Bonjour') ,'Hello')

    def test_french_to_english_good_morning(self):
        self.assertEqual(french_to_english("J'espère que vous allez bien !") ,"Good morning!")


if __name__ == '__main__':
    unittest.main()