
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    df = pd.read_csv('/home/ubuntu/cleaned_books_dataset.csv')
    
    # Set style
    sns.set_theme(style="whitegrid")
    
    # 1. Price Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price (£)'], bins=10, kde=True, color='skyblue')
    plt.title('Distribution of Book Prices')
    plt.xlabel('Price (£)')
    plt.ylabel('Frequency')
    plt.savefig('/home/ubuntu/price_distribution.png')
    plt.close()
    
    # 2. Rating Distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Rating (1-5)', data=df, palette='viridis')
    plt.title('Distribution of Book Ratings')
    plt.xlabel('Rating (1-5)')
    plt.ylabel('Count')
    plt.savefig('/home/ubuntu/rating_distribution.png')
    plt.close()
    
    # 3. Price vs Rating (Boxplot)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Rating (1-5)', y='Price (£)', data=df, palette='Set2')
    plt.title('Book Prices by Rating')
    plt.xlabel('Rating (1-5)')
    plt.ylabel('Price (£)')
    plt.savefig('/home/ubuntu/price_by_rating.png')
    plt.close()
    
    # 4. Price vs Rating (Scatter Plot)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Rating (1-5)', y='Price (£)', data=df, s=100, color='coral')
    plt.title('Scatter Plot: Price vs Rating')
    plt.xlabel('Rating (1-5)')
    plt.ylabel('Price (£)')
    plt.savefig('/home/ubuntu/price_vs_rating_scatter.png')
    plt.close()

if __name__ == "__main__":
    create_visualizations()