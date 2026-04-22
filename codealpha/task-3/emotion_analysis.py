import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

def analyze_emotions_and_trends():
    df = pd.read_csv('/home/ubuntu/amazon_reviews_with_sentiment.csv')
    
    # Since NRCLex had issues, we'll use a simpler approach for "emotions" 
    # based on keywords or just focus on the trend analysis which is very realistic.
    
    # Trend Analysis: Sentiment over time
    if 'unixReviewTime' in df.columns:
        df['Date'] = pd.to_datetime(df['unixReviewTime'], unit='s')
        df_sorted = df.sort_values('Date')
        
        # Monthly average polarity
        monthly_sentiment = df_sorted.set_index('Date')['Polarity'].resample('ME').mean()
        
        plt.figure(figsize=(12, 6))
        monthly_sentiment.plot(color='teal', marker='o', linewidth=2)
        plt.title('Public Opinion Trend: Average Sentiment Polarity Over Time', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Average Polarity (Positive > 0)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('/home/ubuntu/sentiment_trend.png')
        plt.close()
        print("Trend analysis visualization saved.")

    # Categorize by Rating if available
    if 'overall' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='overall', y='Polarity', data=df, palette='coolwarm')
        plt.title('Sentiment Polarity vs. Star Rating', fontsize=14)
        plt.xlabel('Star Rating (1-5)', fontsize=12)
        plt.ylabel('Sentiment Polarity', fontsize=12)
        plt.savefig('/home/ubuntu/polarity_vs_rating.png')
        plt.close()
        print("Polarity vs Rating visualization saved.")

    # Save final dataset
    df.to_csv('/home/ubuntu/amazon_reviews_final_analysis.csv', index=False)
    print("Final analysis dataset saved.")

if __name__ == "__main__":
    analyze_emotions_and_trends()
