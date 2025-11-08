import pandas as pd


def preprocess_data(df):

    df = df.drop(columns=['Rk']) #additional column
    df[['Gtm', 'Tm', 'Opp.1']]=df[['Gtm', 'Tm', 'Opp.1']].astype('int64') 
    df = df.sort_values("Date") #time series --> index order = date order
    df = df.reset_index(drop=True)

    # Define numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()



    # Create preprocessing pipelines for numerical and categorical data
    #numerical_pipeline = Pipeline(steps=[
      #  ('imputer', SimpleImputer(strategy='mean')),
     #   ('scaler', StandardScaler())
   # ])

    #categorical_pipeline = Pipeline(steps=[
   #     ('imputer', SimpleImputer(strategy='most_frequent')),
   #     ('onehot', OneHotEncoder(handle_unknown='ignore'))
   # ])

    # Combine preprocessing pipelines
    #preprocessor = ColumnTransformer(
     #   transformers=[
     #       ('num', numerical_pipeline, numerical_cols),
      #      ('cat', categorical_pipeline, categorical_cols)
      #  ]
   # )

    # Apply the preprocessing
    #processed_data = preprocessor.fit_transform(df)

    return df, numerical_cols, categorical_cols

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    return preprocess_data(df)