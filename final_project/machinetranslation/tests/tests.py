import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def testFrenchToEnglish(self):
        self.assertIsNone(frenchToEnglish(None))
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

    def testEnglishToFrench(self):
        self.assertIsNone(englishToFrench(None))
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

if __name__ == '__main__':
    unittest.main()