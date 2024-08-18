import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Clean the data by handling missing values."""
    df.fillna(df.mean(), inplace=True)
    return df

def save_data(df, filepath):
    """Save cleaned data to a CSV file."""
    df.to_csv(filepath, index=False)

