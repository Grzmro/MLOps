import joblib
from sklearn.datasets import load_iris


def load_model(path="models/iris_model.joblib"):
    return joblib.load(path)


def predict(model, features):
    prediction = model.predict([features])[0]
    return str(load_iris().target_names[prediction])
