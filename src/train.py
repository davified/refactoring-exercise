import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rnd
# data visualization
import seaborn as sns
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
# machine learning packages
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def prepare_data_and_train_model():
    train_df = pd.read_csv("./input/train.csv")
    test_df = pd.read_csv("./input/test.csv")
    df = pd.concat([train_df, test_df])
    df.head()
    df = df.drop(['Ticket', 'Cabin'], axis=1)

    # [code smell] - Exposed Internals
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col',
                                       'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace(['Ms', 'Mlle'], 'Miss')
    df['Title'] = df['Title'].replace(['Mme'], 'Mrs')
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    df['Title'] = df['Title'].map(title_mapping)
    df['Title'] = df['Title'].fillna(0)

    # [code smell] Duplicate Responsibility - df.drop() happens at multiple places.
    # it would be better if they were consolidated
    df = df.drop(['Name', 'PassengerId'], axis=1)

    # [code smell] Duplicate Responsibility again - encoding of string variables into integers
    # should be consolidated into one place
    df['Sex'] = df['Sex'].map({'female': 1, 'male': 0}).astype(int)

    # [code smell] Dead Code - 'AgeBand' column is defined but never used
    df['AgeBand'] = pd.cut(df['Age'], 5)

    # [code smell] - magic numbers: 16, 32, 48
    df.loc[df['Age'] <= 16, 'Age'] = 0
    df.loc[(df['Age'] > 16) & (df['Age'] <= 32), 'Age'] = 1
    df.loc[(df['Age'] > 32) & (df['Age'] <= 48), 'Age'] = 2
    df.loc[(df['Age'] > 48) & (df['Age'] <= 64), 'Age'] = 3
    df = df.drop(['AgeBand'], axis=1)

    # [code smell] Exposed Internals - the next 2 cells could be extracted into a function
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1
    df = df.drop(['Parch', 'SibSp', 'FamilySize'], axis=1)
    freq_port = df.Embarked.dropna().mode()[0]
    df['Embarked'] = df['Embarked'].fillna(freq_port)
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)

    # [code smell] Duplicate Responsibility - filling nans with the median value has been done in a cell above
    df['Age'] = df['Age'].fillna(df['Age'].dropna().median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].dropna().median())

    # [code smell] Duplication - this looks almost identical to the cells that convert 'Age' from continuous variables to categorical variables
    df['FareBand'] = pd.qcut(df['Fare'], 4)
    df.loc[df['Fare'] <= 7.91, 'Fare'] = 0
    df.loc[(df['Fare'] > 7.91) & (df['Fare'] <= 14.454), 'Fare'] = 1
    df.loc[(df['Fare'] > 14.454) & (df['Fare'] <= 31), 'Fare'] = 2
    df.loc[df['Fare'] > 31, 'Fare'] = 3
    df['Fare'] = df['Fare'].astype(int)
    df = df.drop(['FareBand'], axis=1)

    train_df = df[-df['Survived'].isna()]
    test_df = df[df['Survived'].isna()]
    test_df = test_df.drop('Survived', axis=1)
    X_train = train_df.drop("Survived", axis=1)
    Y_train = train_df["Survived"]
    X_test = test_df.copy()

    random_forest = RandomForestClassifier(n_estimators=100)
    random_forest.fit(X_train, Y_train)
    Y_pred = random_forest.predict(X_test)
    random_forest.score(X_train, Y_train)
    acc_random_forest = round(random_forest.score(X_train, Y_train) * 100, 2)

    return random_forest, X_train, Y_train


prepare_data_and_train_model()
