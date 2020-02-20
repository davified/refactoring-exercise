def train_model(ModelClass, X_train, Y_train, X_test, **kwargs):
    model = ModelClass(**kwargs)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy_score = round(model.score(X_train, Y_train) * 100, 2)
    accuracy_score

    return model, accuracy_score

def add(n1, n2):
    return n1 + n2

def multiply_by_10(df):
    for col in df.columns:
        if df.dtypes[col] != 'object':
            df[col] = df[col] * 10
    
    return df

def impute_nans(df, columns):
    for col in columns:
        if df.dtypes[col] != 'object':
            df[col] = df[col].fillna(df[col].dropna().median())
        
    return df