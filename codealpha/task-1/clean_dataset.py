import pandas as pd
import re

def clean_data():
    input_file = '/home/ubuntu/books_dataset.csv'
    output_file = '/home/ubuntu/cleaned_books_dataset.csv'
    
    df = pd.read_csv(input_file)
    
    # Clean Price: Use regex to extract numeric value
    df['Price (£)'] = df['Price'].apply(lambda x: float(re.findall(r"[-+]?\d*\.\d+|\d+", x)[0]))
    
    # Map Rating: Convert text rating to numeric
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    df['Rating (1-5)'] = df['Rating'].map(rating_map)
    
    # Drop original Price and Rating columns
    df = df.drop(columns=['Price', 'Rating'])
    
    # Reorder columns
    df = df[['Title', 'Price (£)', 'Rating (1-5)', 'Availability']]
    
    # Save cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved to {output_file}")
    print("\nSample Data:")
    print(df.head())

if __name__ == "__main__":
    clean_data()
