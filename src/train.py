import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from preprocessing import (add_categorical_columns, add_derived_title,
                           add_is_alone_column, categorize_column, impute_nans, 
                           train_model)
                           
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

rf_model, accuracy_random_forest = train_model(
    RandomForestClassifier, X, Y, n_estimators=100)

# if necessary, pickle rf_model for further testing / deployment
