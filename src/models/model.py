from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

class NBAOutcomePredictor:
    def __init__(self, model_type='random_forest'):
        if model_type == 'random_forest':
            self.model = RandomForestClassifier()
        elif model_type == 'logistic_regression':
            self.model = LogisticRegression()
        else:
            raise ValueError("Unsupported model type. Choose 'random_forest' or 'logistic_regression'.")
        self.scaler = StandardScaler()

    def fit(self, X, y):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def predict_proba(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)

    def score(self, X, y):
        X_scaled = self.scaler.transform(X)
        return self.model.score(X_scaled, y)