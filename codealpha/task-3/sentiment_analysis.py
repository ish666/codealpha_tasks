import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sentiment():
    # Load the real dataset
    df = pd.read_csv('/home/ubuntu/amazon_reviews.csv')
    
    # Preprocessing: Drop rows with missing reviewText
    df = df.dropna(subset=['reviewText'])
    
    # Perform Sentiment Analysis using TextBlob
    def get_sentiment(text):
        analysis = TextBlob(str(text))
        # Polarity is a float within the range [-1.0, 1.0]
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'
    
    def get_polarity(text):
        return TextBlob(str(text)).sentiment.polarity

    print("Analyzing sentiments...")
    df['Sentiment'] = df['reviewText'].apply(get_sentiment)
    df['Polarity'] = df['reviewText'].apply(get_polarity)
    
    # Save the results
    df.to_csv('/home/ubuntu/amazon_reviews_with_sentiment.csv', index=False)
    
    # Summary Statistics
    print("\n--- Sentiment Distribution ---")
    print(df['Sentiment'].value_counts())
    
    # Visualization: Sentiment Distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Sentiment', data=df, palette='viridis', order=['Positive', 'Neutral', 'Negative'])
    plt.title('Sentiment Distribution of Amazon Reviews')
    plt.savefig('/home/ubuntu/sentiment_distribution.png')
    plt.close()
    
    # Visualization: Polarity Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Polarity'], bins=30, kde=True, color='blue')
    plt.title('Polarity Distribution of Amazon Reviews')
    plt.savefig('/home/ubuntu/polarity_distribution.png')
    plt.close()
    
    print("\nAnalysis complete. Results saved to /home/ubuntu/amazon_reviews_with_sentiment.csv")

if __name__ == "__main__":
    analyze_sentiment()
