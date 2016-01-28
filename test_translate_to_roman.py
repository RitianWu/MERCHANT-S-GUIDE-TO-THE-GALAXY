import unittest
from translater import *


class TranslaterTestCase(unittest.TestCase):
    """Tests for `translater.py`."""

    def test_translate_to_roman(self):
        translater = Translater()
        self.assertTrue(translater.translate_to_roman("glob prok"))

    def test_translate_to_num(self):
        translater = Translater()
        self.assertTrue(translater.translate_to_num("MCMIII"))

if __name__ == '__main__':
    unittest.main()
