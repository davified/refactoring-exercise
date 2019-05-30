import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from src.preprocessing import add_derived_title, encode_title


class TestProcessing(unittest.TestCase):
    def test_add_derived_title(self):
        df = pd.DataFrame({
            'Name': ['Smith, Mr. Owen Harris	', 'Heikkinen, Miss. Laina	', 'Allen, Mlle. Maisie',
                     'Allen, Ms. Maisie', 'Allen, Mme. Maisie',

                     # rare titles
                     'Smith, Lady. Owen Harris	', 'Heikkinen, Countess. X	', 'Allen, Capt. Maisie',
                     'Smith, Col. Owen Harris	', 'Heikkinen, Don. Laina	', 'Allen, Dr. Maisie',
                     'Smith, Major. Owen Harris	', 'Heikkinen, Rev. Laina	', 'Allen, Sir. Maisie',
                     'Smith, Jonkheer. Owen Bob	', 'Heikkinen, Dona. Laina	'
                     ],

        })

        expected = pd.DataFrame({
            'Name': ['Smith, Mr. Owen Harris	', 'Heikkinen, Miss. Laina	', 'Allen, Mlle. Maisie',
                     'Allen, Ms. Maisie', 'Allen, Mme. Maisie',

                     'Smith, Lady. Owen Harris	', 'Heikkinen, Countess. X	', 'Allen, Capt. Maisie',
                     'Smith, Col. Owen Harris	', 'Heikkinen, Don. Laina	', 'Allen, Dr. Maisie',
                     'Smith, Major. Owen Harris	', 'Heikkinen, Rev. Laina	', 'Allen, Sir. Maisie',
                     'Smith, Jonkheer. Owen Bob	', 'Heikkinen, Dona. Laina	'
                     ],
            'Title': ['Mr', 'Miss', 'Miss',
                      'Miss', 'Mrs',

                      'Rare', 'Rare', 'Rare',
                      'Rare', 'Rare', 'Rare',
                      'Rare', 'Rare', 'Rare',
                      'Rare', 'Rare']
        })

        assert_frame_equal(expected, add_derived_title(df))

    def test_encode_title(self):
        df = pd.DataFrame({'Title': ['Mr', 'Miss', 'Miss', 'Mrs',
                                     'Miss', 'Rare', 'Rare', np.nan]
                           })

        expected = pd.DataFrame({
            'Title': [1, 2, 2, 3, 2, 5, 5, 0]
        })
        assert_frame_equal(expected, encode_title(df), check_dtype=False)
        
