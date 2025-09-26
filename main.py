import requests

def fetch_games():
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def filter_games(games, search_term):
    search_term_lower = search_term.lower()
    return [game for game in games if search_term_lower in game['title'].lower()]

def display_game_list(matching_games):
    if not matching_games:
        print("That game doesn't exist pal")
        return
    print("Matching games:")
    for i, game in enumerate(matching_games, start=1):
        print(f"{i}. {game['title']} (ID: {game['id']})")
        print(f"Genre: {game['genre']}")
        print(f"Platform: {game['platform']}")
        print(f"Short Description: {game['short_description']}")
        print()

def main():
    print("FreeToGame app Jumpscare!!!")
    search_term = input("Search for a game:").strip()
    if not search_term:
        print("Try again buddy")
        return
    try:
        all_games = fetch_games()
        matching_games = filter_games(all_games, search_term)
        display_game_list(matching_games)
    except requests.RequestException as e:
        print(f"Couldn't from data from api: {e}")

if __name__ == "__main__":
    main()