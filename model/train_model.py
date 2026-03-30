import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    # Load dataset (use your existing dataset here)
    data = pd.read_csv("data/KDDTrain+.txt", header=None)

    # Features and labels
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # One-hot encoding
    X = pd.get_dummies(X)
    X.columns = X.columns.astype(str)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    return model, X_test, y_test