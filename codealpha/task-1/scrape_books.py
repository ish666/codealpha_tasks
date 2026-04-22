import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    
    book_data = []
    
    for book in books:
        # Extract Title
        title = book.h3.a['title']
        
        # Extract Price
        price = book.find('p', class_='price_color').text
        
        # Extract Rating
        # The rating is in the class of the <p> tag, e.g., "star-rating Three"
        rating_classes = book.find('p', class_='star-rating')['class']
        rating = [c for c in rating_classes if c != 'star-rating'][0]
        
        # Extract Availability
        availability = book.find('p', class_='instock availability').text.strip()
        
        book_data.append({
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Availability': availability
        })
    
    # Save to CSV
    output_file = '/home/ubuntu/books_dataset.csv'
    keys = book_data[0].keys()
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(book_data)
    
    print(f"Successfully scraped {len(book_data)} books and saved to {output_file}")

if __name__ == "__main__":
    scrape_books()
