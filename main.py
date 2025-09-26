import requests

def fetch_games():
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    print("FreeToGame App Jumpscare!!!")
    try:
        all_games = fetch_games()
        print(f"Gathered {len(all_games)} games")
    except requests.RequestException as e:
        print(f"Couldn't get data from api: {e}")
if __name__ == "__main__":
    main()