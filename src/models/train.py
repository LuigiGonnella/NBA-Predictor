from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import joblib
from src.models.model import create_model
from src.data.preprocess import preprocess_data
from src.utils.metrics import calculate_metrics

def train_model(data, target_column, n_splits=5):
    X = data.drop(columns=[target_column])
    y = data[target_column]

    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    fold_results = []

    for train_index, val_index in kf.split(X):
        X_train, X_val = X.iloc[train_index], X.iloc[val_index]
        y_train, y_val = y.iloc[train_index], y.iloc[val_index]

        model = create_model()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_val)
        accuracy = accuracy_score(y_val, y_pred)
        fold_results.append(accuracy)

    mean_accuracy = np.mean(fold_results)
    print(f'Mean Accuracy: {mean_accuracy:.4f}')
    return model

def main():
    data_path = 'data/processed/processed_data.csv'
    target_column = 'outcome'  # Replace with your actual target column name

    data = pd.read_csv(data_path)
    processed_data = preprocess_data(data)

    trained_model = train_model(processed_data, target_column)
    joblib.dump(trained_model, 'models/trained_model.pkl')

if __name__ == "__main__":
    main()