import requests
import json

base_url = "https://store.steampowered.com/api/appdetails?appids="

def load_json(gm):
    with open("config.json", "r", encoding="UTF-8") as file:
        json_data = json.load(file)
    return json_data.get(gm)

def get_info(game):
    id = load_json(game)["id"]
    url = base_url + id + "&cc=pl"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Gra nie istnieje {response.status_code}")
        return None
    prefix = response.json()[id]["data"]
    price_overview = prefix["price_overview"]
    return {
        "name": prefix["name"],
        "current_price": price_overview["final"] / 100,  #
        "old_price": price_overview["initial"] / 100,
        "discount_percent": price_overview["discount_percent"],
    }

def send_to_discord(game_info):
    print("wysyłam", game_info)

def check_price_and_notify(game_name):
    info = get_info(game_name)
    if info is None:
        return

    threshold = float(load_json(game_name).get("threshold"))
    if info["current_price"] < threshold:
        send_to_discord(info)
    else:
        print("cena jest ponad norme")


print(check_price_and_notify("Dying Light 2 Stay Human: Reloaded Edition"))
