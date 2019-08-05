import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.workshop import add_derived_title


class TestWorkshop(unittest.TestCase):
    def test_extract_title_from_name(self):
        df = pd.DataFrame({
            'Name': ['Braund, Mr. Owen Harris', 'Heikkinen, Miss. Laina	', 'Allen, Mlle. Maisie',
                     'Allen, Ms. Maisie', 'Allen, Mme. Maisie', 
                     
                     # rare titles
                     'Smith, Lady. Owen Harris	', 'Heikkinen, Countess. X	', 'Allen, Capt. Maisie',
                     'Smith, Col. Owen Harris	', 'Heikkinen, Don. Laina	', 'Allen, Dr. Maisie',
                     'Smith, Major. Owen Harris	', 'Heikkinen, Rev. Laina	', 'Allen, Sir. Maisie',
                     'Smith, Jonkheer. Owen Bob	', 'Heikkinen, Dona. Laina	']
        })

        expected = pd.DataFrame({
            'Name': ['Braund, Mr. Owen Harris', 'Heikkinen, Miss. Laina	', 'Allen, Mlle. Maisie',
                     'Allen, Ms. Maisie', 'Allen, Mme. Maisie', 
                     
                     # rare titles
                     'Smith, Lady. Owen Harris	', 'Heikkinen, Countess. X	', 'Allen, Capt. Maisie',
                     'Smith, Col. Owen Harris	', 'Heikkinen, Don. Laina	', 'Allen, Dr. Maisie',
                     'Smith, Major. Owen Harris	', 'Heikkinen, Rev. Laina	', 'Allen, Sir. Maisie',
                     'Smith, Jonkheer. Owen Bob	', 'Heikkinen, Dona. Laina	'],
            'Title': ['Mr', 'Miss', 'Miss', 'Miss', 'Mrs', 
                      
                      'Rare', 'Rare', 'Rare',
                      'Rare', 'Rare', 'Rare',
                      'Rare', 'Rare', 'Rare',
                      'Rare', 'Rare']
        })

        assert_frame_equal(expected, add_derived_title(df))
