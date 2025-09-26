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

def get_user_selection(matching_games):
    if not matching_games:
        return None
    while True:
        try:
            choice = int(input("Select a game by number: "))
            if choice == 0:
                return None
            if 1 <= choice <= len(matching_games):
                return matching_games[choice - 1]['id']
            else:
                print("Not on the list buddy")
        except ValueError:
            print("A number. NUMBER")

def fetch_game_details(game_id):
    url = f"https://www.freetogame.com/api/game?id={game_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def display_game_details(game_details):
    game = game_details['game'] if 'game' in game_details else game_details
    print(f"\nGame Details:")
    print(f"Title: {game.get('title', 'N/A')}")
    print(f"Genre: {game.get('genre', 'N/A')}")
    print(f"Platform: {game.get('platform', 'N/A')}")
    print(f"Publisher: {game.get('publisher', 'N/A')}")
    print(f"Developer: {game.get('developer', 'N/A')}")
    print(f"Release Date: {game.get('release_date', 'N/A')}")
    print(f"Status: {game.get('status', 'N/A')}")
    print(f"Description: {game.get('description', 'N/A')}")
    
    if game.get('minimum_system_requirements'):
        req = game['minimum_system_requirements']
        print("\nMinimum System Requirements:")
        print(f"OS: {req.get('os', 'N/A')}")
        print(f"Processor: {req.get('processor', 'N/A')}")
        print(f"Memory: {req.get('memory', 'N/A')}")
        print(f"Graphics: {req.get('graphics', 'N/A')}")
        print(f"Storage: {req.get('storage', 'N/A')}")
    
    if game.get('screenshots'):
        print("\nScreenshots:")
        for screenshot in game['screenshots']:
            print(f"- {screenshot.get('image', 'N/A')}")

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
        selected_id = get_user_selection(matching_games)
        if selected_id is None:
            print("Exiting.")
            return
        details = fetch_game_details(selected_id)
        display_game_details(details)
    except requests.RequestException as e:
        print(f"Couldn't get data from api: {e}")
    except Exception as e:
        print(f"Oopsie somewhere {e}")

if __name__ == "__main__":
    main()