import pytest
import pandas as pd
import numpy as np
from src.cancer_mlp_engine import BreastCancerMLPEngine

def test_mlp_cancer_engine():
    X = pd.DataFrame(np.random.rand(20, 9), columns=[f"feat_{i}" for i in range(9)])
    y = pd.Series(np.random.choice([2, 4], size=20))
    
    engine = BreastCancerMLPEngine()
    engine.fit(X, y)
    preds = engine.predict(X)
    
    assert len(preds) == 20
    assert np.all(np.isin(preds, [2, 4]))
