import unittest
from translater import *


class TranslaterTestCase(unittest.TestCase):
    """Tests for `translater.py`."""

    def test_translate_to_roman(self):
        translater = Translater()
        self.assertTrue(translater.translate_to_roman("glob prok"))

    def test_translate_to_num(self):
        info_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        translater = Translater(info_roman=info_roman)
        print translater.translate_to_num("XXXID")
        self.assertTrue(translater.translate_to_num("MCMIII"))

if __name__ == '__main__':
    unittest.main()
