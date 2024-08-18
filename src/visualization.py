import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=30, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def main():
    df = pd.read_csv('../data/processed/cleaned_data.csv')
    plot_age_distribution(df)
    plot_correlation_heatmap(df)

if __name__ == '__main__':
    main()
