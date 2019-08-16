import unittest

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from pandas.testing import assert_frame_equal, assert_series_equal

from src.preprocessing import (add_derived_title, add_is_alone_column,
                               categorize_column, impute_nans, train_model)


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

    def test_categorize_column_into_2_categories(self):
        series = pd.Series([5, 20, 10, 25])  # bins:  [ 4.98 15.   25.  ]

        assert_series_equal(
            pd.Series([1, 2, 1, 2]), categorize_column(series, num_bins=2))

    def test_categorize_column_into_5_categories(self):
        # bins: [ -0.1,  20. ,  40. ,  60. ,  80. , 100. ]
        series = pd.Series([0, 30, 50, 80, 100])

        assert_series_equal(
            pd.Series([1, 2, 3, 4, 5]), categorize_column(series, num_bins=5))

    def test_add_is_alone_column(self):
        # df = df['SibSp'] + df['Parch']
        df = pd.DataFrame({
            'SibSp': [0, 1, 2, 0, 0],
            'Parch': [0, 0, 5, 0, 1]
        })

        expected = pd.DataFrame({
            'SibSp':   [0, 1, 2, 0, 0],
            'Parch':   [0, 0, 5, 0, 1],
            'IsAlone': [1, 0, 0, 1, 0]
        })

        print(add_is_alone_column(df))
        assert_frame_equal(expected, add_is_alone_column(df))

    def test_impute_nans_for_categorical_columns_replaces_na_with_most_frequent_mode(self):
        df = pd.DataFrame({
            'some_categorical_column': ['A', 'A', 'B', np.nan, 'A', np.nan]
        })

        expected = pd.DataFrame({
            'some_categorical_column': ['A', 'A', 'B', 'A', 'A', 'A']
        })

        assert_frame_equal(expected, impute_nans(
            df, categorical_columns=['some_categorical_column']))

    def test_impute_nans_for_continuous_columns_replaces_na_with_median(self):
        df = pd.DataFrame({
            # median value: 20
            'some_continuous_column': [10, 20, np.nan, np.nan, 30]
        })

        expected = pd.DataFrame({
            'some_continuous_column': [10, 20, 20, 20, 30]
        })

        assert_frame_equal(expected, impute_nans(df, continuous_columns=[
                           'some_continuous_column']), check_dtype=False)


    def test_train_model_should_return_instance_of_model_and_accuracy_score(self):
        model, accuracy = train_model(DecisionTreeClassifier, [[1, 1, 1], [1, 1, 1]], [0, 1])

        self.assertIsInstance(model, DecisionTreeClassifier)
        self.assertIsInstance(accuracy, float)