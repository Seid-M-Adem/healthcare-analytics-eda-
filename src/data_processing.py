import pandas as pd

def clean_data(df):
    # Example of data cleaning process
    df.fillna(df.mean(), inplace=True)
    df.dropna(inplace=True)
    # Additional cleaning steps
    return df

def save_data(df, path):
    df.to_csv(path, index=False)

def main():
    df = pd.read_csv('../data/raw/healthcare_dataset.csv')
    df_cleaned = clean_data(df)
    save_data(df_cleaned, '../data/processed/cleaned_data.csv')

if __name__ == '__main__':
    main()

