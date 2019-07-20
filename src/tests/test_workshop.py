import unittest
import pandas as pd
import numpy as np
from src.workshop import add, impute_nans
from pandas.testing import assert_frame_equal


class TestWorkshop(unittest.TestCase):
    def test_impute_nans_should_fill_nans_with_median_value(self):
        # arrange
        df = pd.DataFrame({
            'some_column': [1, np.nan]
        })
        expected = pd.DataFrame({
            'some_column': [1., 1.]
        })

        # act
        actual = impute_nans(df, columns=['some_column'])

        # assert
        assert_frame_equal(expected, actual)


    def test_df_should_equal_itself(self):
        # arrange
        df = pd.DataFrame({
            'column_1': [1, 2, 3]
        })

        # assert
        assert_frame_equal(df, df)

    def test_add_1_and_1_should_return_2(self):
        # arrange
        expected = 2

        # act
        actual = add(1, 1)

        # assert
        self.assertEqual(expected, actual)