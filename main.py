import os
import random
from typing import List, Set
from scraper import scrape_artists_from_url

class MusicManager:
    def __init__(self):
        self.try_file = "music-to-try.txt"
        self.ignore_file = "music-to-ignore.txt"
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        """Ensure both text files exist."""
        for file in [self.try_file, self.ignore_file]:
            if not os.path.exists(file):
                open(file, 'w').close()

    def _read_artists(self, filename: str) -> Set[str]:
        """Read artists from a file and return as a set."""
        with open(filename, 'r') as f:
            return {line.strip() for line in f if line.strip()}

    def _write_artists(self, filename: str, artists: Set[str]):
        """Write artists to a file."""
        with open(filename, 'w') as f:
            for artist in sorted(artists):
                f.write(f"{artist}\n")

    def add_source(self, url: str):
        """Add artists from a Sputnik Music source URL."""
        try:
            # Get new artists from the URL
            new_artists = scrape_artists_from_url(url)
            
            # Get existing artists
            try_artists = self._read_artists(self.try_file)
            ignore_artists = self._read_artists(self.ignore_file)
            
            # Add new artists, excluding those in ignore list
            try_artists.update(new_artists - ignore_artists)
            
            # Save updated list
            self._write_artists(self.try_file, try_artists)
            print(f"Added {len(new_artists)} new artists to try")
            
        except Exception as e:
            print(f"An error occurred: {e}")

    def try_music(self):
        """Get a random artist to try."""
        try_artists = self._read_artists(self.try_file)
        if not try_artists:
            print("No artists left to try!")
            return

        artist = random.choice(list(try_artists))
        print(f"\nArtist to try: {artist}")
        
        while True:
            response = input("Have you checked this artist? (y/n): ").lower()
            if response in ['y', 'n']:
                break
            print("Please answer 'y' or 'n'")

        if response == 'y':
            try_artists.remove(artist)
            ignore_artists = self._read_artists(self.ignore_file)
            ignore_artists.add(artist)
            
            self._write_artists(self.try_file, try_artists)
            self._write_artists(self.ignore_file, ignore_artists)
            print(f"Added {artist} to ignore list")

def main():
    manager = MusicManager()
    
    while True:
        print("\n=== Music Manager ===")
        print("1. Add source")
        print("2. Try music")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            url = input("Enter Sputnik Music URL: ")
            manager.add_source(url)
        elif choice == "2":
            manager.try_music()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 