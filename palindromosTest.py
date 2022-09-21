import unittest
from palindromos import palindromo

class TestPalidnromos(unittest.TestCase):

    def test_par(self):
        self.assertTrue(palindromo("otto"))

    def test_impar(self):
        self.assertTrue(palindromo("neuquen"))

if __name__ == '__main__':
    unittest.main() 