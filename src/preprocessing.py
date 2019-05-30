def add_derived_title(df):
    titles = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    
    titles = titles.replace(['Lady', 'Countess','Capt', 'Col',\
                                    'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    titles = titles.replace(['Ms', 'Mlle'], 'Miss')
    titles = titles.replace(['Mme'], 'Mrs')

    df['Title'] = titles

    return df

def encode_title(df):
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

    df['Title'] = df['Title'].map(title_mapping).fillna(0)

    return df