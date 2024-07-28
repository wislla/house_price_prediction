import pandas as pd


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:

    data = data.fillna(method='ffill')  # type: ignore    return data
    return data