import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    """Plot the distribution of ages."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], kde=True)
    plt.title('Age Distribution')
    plt.show()

def plot_correlation_heatmap(df):
    """Plot a heatmap of correlations between features."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

