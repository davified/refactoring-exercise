def add(a, b):
    return a + b

def impute_nans(df, columns):
    for column in columns:
        df[column] = df[column].fillna(df[column].dropna().median())

    return df