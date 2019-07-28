import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from model_training import train_model
from preprocessing import (add_categorical_columns, add_derived_title,
                           add_is_alone_column, categorize_column, impute_nans)

train_df = pd.read_csv("./input/train.csv")
test_df = pd.read_csv("./input/test.csv")
df = pd.concat([train_df, test_df], sort=True)

df = impute_nans(df, categorical_columns=[
                 'Embarked'], continuous_columns=['Fare', 'Age'])
df = add_derived_title(df)
df = add_is_alone_column(df)
df = add_categorical_columns(df)

df['AgeGroup*Class'] = df['AgeGroup'] * df['Pclass']
df = df.drop(['Parch', 'SibSp', 'Name', 'PassengerId',
              'Ticket', 'Cabin'], axis=1)

train_df = df[-df['Survived'].isna()]
X_train = train_df.drop("Survived", axis=1)
Y_train = train_df["Survived"]

rf_model, accuracy_random_forest = train_model(
    RandomForestClassifier, X_train, Y_train, n_estimators=100)

# if necessary, pickle rf_model for further testing / deployment
