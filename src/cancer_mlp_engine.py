import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

class BreastCancerMLPEngine:
    def __init__(self, random_state: int = 42):
        self.scaler = StandardScaler()
        self.model = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=random_state)
        self.feature_cols = None

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.feature_cols = X.columns.tolist()
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        X_scaled = self.scaler.transform(X[self.feature_cols])
        return self.model.predict(X_scaled)
