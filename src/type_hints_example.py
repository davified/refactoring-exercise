from typing import List
import pandas as pd

# def tokenize(strings):
#     return [s.split() for s in strings]

def tokenize(strings: List[str]) -> List[List[str]]:
    return [s.split() for s in strings]

x = tokenize([1])

# def create_dataframe(column_1_values, column_2_values):
#     return pd.DataFrame(column_1_values, column_2_values)

# def create_dataframe(column_1_values: List[str], column_2_values: List[float]) -> pd.DataFrame:
#     return pd.DataFrame(column_1_values, column_2_values)

# x = create_dataframe(['bob', 'jane', 'mary'], [25, 30, 35])

# if type hints isn't working right for you in VS code, read this: https://stackoverflow.com/questions/52155987/python-3-x-type-hints-in-visual-studio-code

