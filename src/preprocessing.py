import pandas as pd
import numpy as np

def add_derived_title(df):
    titles = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)

    titles = titles.replace(['Lady', 'Countess', 'Capt', 'Col',
                             'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    titles = titles.replace(['Ms', 'Mlle'], 'Miss')
    titles = titles.replace(['Mme'], 'Mrs')

    df['Title'] = titles

    return df


def encode_title(df):
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

    df['Title'] = df['Title'].map(title_mapping).fillna(0)

    return df


def categorize_column(series, num_bins):
    bins = pd.cut(series, num_bins, retbins=True)[1]
    return pd.Series(np.digitize(series, bins, right=True))


def add_is_alone_column(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    df['IsAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1

    df = df.drop(['FamilySize'], axis = 1)

    return df

def impute_nans(df, categorical_columns=[], continuous_columns=[]):
    for column in categorical_columns + continuous_columns:
        if column in categorical_columns:
            replacement = df[column].dropna().mode()[0]
        if column in continuous_columns:
            replacement = df[column].dropna().median()
        df[column] = df[column].fillna(replacement)
    
    return df
