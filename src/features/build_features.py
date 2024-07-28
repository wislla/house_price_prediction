import pandas as pd


def build_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create features from the raw data.

    :param data: DataFrame containing the raw data.
    :return: DataFrame with new features.
    """
    # Example feature: total rooms
    data['TotalRooms'] = (
        data['BedroomAbvGr'] + 
        data['KitchenAbvGr'] + 
        data['TotRmsAbvGrd'])
    return data
