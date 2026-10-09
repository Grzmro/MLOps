from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    iris = load_iris()
    return iris.data, iris.target


def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model


def save_model(model, path="models/iris_model.joblib"):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    return path


if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    saved_path = save_model(model)
    print(f"Model saved to {saved_path}")
