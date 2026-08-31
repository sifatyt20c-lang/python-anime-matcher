#!/usr/bin/env python3
"""
Python Anime Matcher
A beginner-friendly tool to recommend anime based on user mood and preferences.
Perfect for Crunchyroll fans!
"""

# Anime Database - Dictionary of popular anime titles by mood
ANIME_DATABASE = {
    "happy": [
        {"title": "Nichijou", "genre": "Comedy, Slice of Life", "episodes": 26, "rating": 8.2},
        {"title": "Kaguya-sama: Love is War", "genre": "Comedy, Romance", "episodes": 12, "rating": 8.7},
        {"title": "Spy x Family", "genre": "Action, Comedy", "episodes": 12, "rating": 8.8},
        {"title": "Mob Psycho 100", "genre": "Comedy, Supernatural", "episodes": 12, "rating": 8.4},
        {"title": "The Devil is a Part-Timer!", "genre": "Comedy, Fantasy", "episodes": 13, "rating": 7.9},
    ],
    "sad": [
        {"title": "Your Name", "genre": "Romance, Drama", "episodes": 1, "rating": 8.4},
        {"title": "Clannad: After Story", "genre": "Drama, Supernatural", "episodes": 25, "rating": 8.9},
        {"title": "A Silent Voice", "genre": "Drama, School", "episodes": 1, "rating": 8.9},
        {"title": "Anohana: The Flower We Saw That Day", "genre": "Drama, Fantasy", "episodes": 11, "rating": 8.3},
        {"title": "Toradora!", "genre": "Romance, Comedy", "episodes": 25, "rating": 7.8},
    ],
    "excited": [
        {"title": "Jujutsu Kaisen", "genre": "Action, Supernatural", "episodes": 24, "rating": 8.5},
        {"title": "Attack on Titan", "genre": "Action, Drama", "episodes": 94, "rating": 8.5},
        {"title": "One Punch Man", "genre": "Action, Comedy", "episodes": 12, "rating": 8.3},
        {"title": "My Hero Academia", "genre": "Action, School", "episodes": 88, "rating": 7.9},
        {"title": "Demon Slayer", "genre": "Action, Supernatural", "episodes": 26, "rating": 8.6},
    ],
    "relaxed": [
        {"title": "Laid-Back Camp", "genre": "Slice of Life, Comedy", "episodes": 12, "rating": 8.3},
        {"title": "A Place Further Than the Universe", "genre": "Adventure, Slice of Life", "episodes": 13, "rating": 8.5},
        {"title": "K-On!", "genre": "Comedy, School", "episodes": 13, "rating": 7.8},
        {"title": "Barakamon", "genre": "Slice of Life, Comedy", "episodes": 12, "rating": 8.2},
        {"title": "Silver Spoon", "genre": "Comedy, School", "episodes": 11, "rating": 7.8},
    ],
    "thoughtful": [
        {"title": "Steins;Gate", "genre": "Sci-Fi, Thriller", "episodes": 24, "rating": 9.0},
        {"title": "Death Note", "genre": "Psychological, Thriller", "episodes": 37, "rating": 8.6},
        {"title": "Code Geass", "genre": "Action, Sci-Fi", "episodes": 50, "rating": 8.2},
        {"title": "The Promised Neverland", "genre": "Drama, Mystery", "episodes": 12, "rating": 8.6},
        {"title": "Parasyte", "genre": "Action, Psychological", "episodes": 24, "rating": 8.2},
    ],
    "romantic": [
        {"title": "Fruits Basket", "genre": "Romance, Comedy", "episodes": 63, "rating": 7.9},
        {"title": "Ouran High School Host Club", "genre": "Romance, Comedy", "episodes": 26, "rating": 8.1},
        {"title": "Horimiya", "genre": "Romance, School", "episodes": 13, "rating": 8.1},
        {"title": "Wotakoi: Love is Hard for Otaku", "genre": "Romance, Comedy", "episodes": 6, "rating": 7.9},
        {"title": "My Dress-Up Darling", "genre": "Romance, Comedy", "episodes": 12, "rating": 8.2},
    ],
}

# Mood descriptions to help users choose
MOOD_DESCRIPTIONS = {
    "happy": "😄 Feel-good, funny, lighthearted shows",
    "sad": "😢 Emotional, touching, thought-provoking stories",
    "excited": "🔥 Action-packed, intense, thrilling adventures",
    "relaxed": "😌 Chill, cozy, slice-of-life experiences",
    "thoughtful": "🧠 Mind-bending, mysterious, psychological thrillers",
    "romantic": "💕 Love stories, romance, and relationships",
}


def display_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print("🎌 Welcome to Python Anime Matcher! 🎌")
    print("="*60)
    print("Find your perfect anime based on your mood!")
    print("="*60 + "\n")


def display_moods():
    """Display all available moods"""
    print("Choose your current mood:\n")
    for i, (mood, description) in enumerate(MOOD_DESCRIPTIONS.items(), 1):
        print(f"{i}. {mood.capitalize():12} - {description}")
    print()


def get_mood_choice():
    """Get user's mood choice"""
    display_moods()
    
    while True:
        try:
            choice = int(input("Enter the number of your mood (1-6): ").strip())
            moods = list(MOOD_DESCRIPTIONS.keys())
            
            if 1 <= choice <= len(moods):
                return moods[choice - 1]
            else:
                print(f"❌ Please enter a number between 1 and {len(moods)}.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")


def display_anime_list(mood):
    """Display anime recommendations for a given mood"""
    animes = ANIME_DATABASE.get(mood, [])
    
    print(f"\n{'='*60}")
    print(f"🎬 Anime Recommendations for '{mood.upper()}' mood:")
    print(f"{'='*60}\n")
    
    for i, anime in enumerate(animes, 1):
        print(f"{i}. {anime['title']}")
        print(f"   Genre: {anime['genre']}")
        print(f"   Episodes: {anime['episodes']}")
        print(f"   Rating: ⭐ {anime['rating']}/10")
        print()


def get_anime_details(mood):
    """Let user select an anime to see more details"""
    animes = ANIME_DATABASE.get(mood, [])
    
    while True:
        try:
            choice = int(input(f"Which anime interests you? (1-{len(animes)}) or 0 to go back: ").strip())
            
            if choice == 0:
                return None
            elif 1 <= choice <= len(animes):
                return animes[choice - 1]
            else:
                print(f"❌ Please enter a number between 0 and {len(animes)}.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")


def display_anime_details(anime):
    """Display detailed information about an anime"""
    print(f"\n{'='*60}")
    print(f"📺 {anime['title'].upper()}")
    print(f"{'='*60}")
    print(f"Genre:     {anime['genre']}")
    print(f"Episodes:  {anime['episodes']}")
    print(f"Rating:    ⭐ {anime['rating']}/10")
    print(f"\n💡 Find it on Crunchyroll and start watching!")
    print(f"{'='*60}\n")


def play_again():
    """Ask if user wants to continue"""
    while True:
        choice = input("Would you like to try another mood? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("❌ Please enter 'yes' or 'no'.\n")


def main():
    """Main function to run the anime matcher"""
    display_welcome()
    
    while True:
        # Get mood from user
        mood = get_mood_choice()
        
        # Display recommendations
        display_anime_list(mood)
        
        # Let user select an anime for details
        selected_anime = get_anime_details(mood)
        if selected_anime:
            display_anime_details(selected_anime)
        
        # Ask if they want to continue
        if not play_again():
            print("\n🎌 Thank you for using Python Anime Matcher!")
            print("Happy watching! 📺✨\n")
            break


if __name__ == "__main__":
    main()
