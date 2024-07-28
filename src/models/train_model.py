import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


def train_model(data: pd.DataFrame, target_column: str) -> LinearRegression:
    """
    Train a linear regression model on the data.

    :param data: DataFrame containing the features and target.
    :param target_column: The name of the target column.
    :return: Trained LinearRegression model.
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.2, 
        random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'model/linear_regression.pkl')
    
    return model
