import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from preprocessing import (add_categorical_columns, add_derived_title,
                           add_is_alone_column, categorize_column, impute_nans, 
                           train_model)

def prepare_data_and_train_model():
    df = pd.read_csv("./input/train.csv")

    df = impute_nans(df, categorical_columns=[
                    'Embarked'], continuous_columns=['Fare', 'Age'])
    df = add_derived_title(df)
    df = add_is_alone_column(df)
    df = add_categorical_columns(df)

    df = df.drop(['Parch', 'SibSp', 'Name', 'PassengerId',
                'Ticket', 'Cabin'], axis=1)

    Y = df["Survived"]
    X = df.drop("Survived", axis=1)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

    rf_model, accuracy_random_forest = train_model(
        RandomForestClassifier, X_train, Y_train, n_estimators=100)

    return rf_model, X_test, Y_test

model, X_test, Y_test = prepare_data_and_train_model()
# if necessary, pickle rf_model for further testing / deployment
