
import pandas as pd
import numpy as np

def perform_eda():
    df = pd.read_csv('/home/ubuntu/cleaned_books_dataset.csv')
    
    # 1. Data Structure
    print("--- Data Structure ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
    # 2. Basic Statistics
    print("\n--- Descriptive Statistics ---")
    stats = df.describe()
    print(stats)
    
    # 3. Value Counts for Categorical Data
    print("\n--- Rating Distribution ---")
    print(df['Rating (1-5)'].value_counts().sort_index())
    
    # 4. Correlation
    print("\n--- Correlation Matrix ---")
    correlation = df[['Price (£)', 'Rating (1-5)']].corr()
    print(correlation)
    
    # 5. Grouped Analysis
    print("\n--- Average Price by Rating ---")
    avg_price_by_rating = df.groupby('Rating (1-5)')['Price (£)'].mean()
    print(avg_price_by_rating)

if __name__ == "__main__":
    perform_eda()