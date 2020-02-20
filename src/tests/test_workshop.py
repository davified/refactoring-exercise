import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from src.workshop import add, multiply_by_10, impute_nans

class TestWorkshop(unittest.TestCase):
    def test_add_1_and_1_should_return_2(self):
        self.assertEquals(2, add(1, 1))
        
    def test_multiply_by_10_should_return_a_df_with_numerical_values_multipled_by_10(self):
        df = pd.DataFrame({
            'age': [1, 2, 3],
            'height': [4, 5, 6],
        })
        expected_df = pd.DataFrame({
            'age': [10, 20, 30],
            'height': [40, 50, 60],
        })
        
        actual_df = multiply_by_10(df)
        
        assert_frame_equal(expected_df, actual_df)
        
    def test_multiply_by_10_does_not_change_string_values(self):
        df = pd.DataFrame({
            'age': [1, 2, 3],
            'names': ['jane', 'bob', 'alice'],
        })
        expected_df = pd.DataFrame({
            'age': [10, 20, 30],
            'names': ['jane', 'bob', 'alice'],
        })
        
        actual_df = multiply_by_10(df)
        
        assert_frame_equal(expected_df, actual_df)
        
    def test_impute_nans_should_replace_nan_values_with_the_median_value(self):
        # arrange
        input_df = pd.DataFrame({
            'column_1': [1, np.nan],
            'column_2': [0, np.nan],
            'column_3': ['hello', 'something'],
        })
        expected_df = pd.DataFrame({
            'column_1': [1, 1],
            'column_2': [0, np.nan],
            'column_3': ['hello', 'something'],
        })
        # act
        actual_df = impute_nans(input_df, columns=['column_1'])
        
        # assert
        assert_frame_equal(expected_df, actual_df, check_dtype=False)