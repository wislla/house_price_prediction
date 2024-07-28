import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    :param file_path: Path to the CSV file.
    :return: DataFrame containing the loaded data.
    """
    return pd.read_csv(file_path)
