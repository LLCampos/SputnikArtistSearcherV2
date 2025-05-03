import requests
from bs4 import BeautifulSoup
from typing import Set
import re

def scrape_artists_from_url(url: str) -> Set[str]:
    """
    Scrape artist names from a Sputnik Music URL, only including artists with albums rated 4.0 or higher.
    
    Args:
        url (str): The Sputnik Music URL to scrape
        
    Returns:
        Set[str]: A set of artist names found on the page with highly rated albums
        
    Raises:
        requests.RequestException: If there's an error fetching the URL
    """
    # Set up headers to look like a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    # Fetch the page content
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all profilebox rows
    profile_boxes = soup.find_all('tr', class_='profilebox')
    print(f"Found {len(profile_boxes)} profile boxes")
    
    artists = set()
    
    for i, box in enumerate(profile_boxes, 1):
        print(f"\nProcessing profile box {i}:")
        
        # Find all text elements in the box
        text_elements = box.find_all(text=True)
        
        # Look for rating text
        for text in text_elements:
            text = text.strip()
            if not text:
                continue
            
            # Extract rating using regex - looking for numbers like 4.0, 4.5, etc.
            rating_match = re.search(r'(\d+\.\d+)', text)
            if rating_match:
                rating = float(rating_match.group(1))
                
                # If rating is 4.0 or higher, find all artist names in sibling elements
                if rating >= 4.0:
                    # Look for artist links in all following sibling rows until we hit another profilebox
                    current_row = box
                    while current_row:
                        current_row = current_row.find_next_sibling('tr')
                        if current_row:
                            # If we hit another profilebox, stop searching
                            if current_row.get('class') and 'profilebox' in current_row.get('class'):
                                break
                                
                            # Look for all artist links in this row
                            artist_links = current_row.find_all('a')
                            for artist_link in artist_links:
                                artist_name = artist_link.find('font', class_='mediumbright')
                                if artist_name:
                                    # Get just the text before the nested font tag
                                    artist_name = artist_name.contents[0].strip()
                                else:
                                    # Fallback to regular text extraction if structure is different
                                    artist_name = artist_link.get_text(strip=True)
                                # Remove any " - " and everything after it (album name)
                                artist_name = artist_name.split(' - ')[0]
                                artists.add(artist_name)
    
    return artists 