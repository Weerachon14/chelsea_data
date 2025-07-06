import json
import os

def find_player_stats(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "playerStats":
                return value
            else:
                result = find_player_stats(value)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = find_player_stats(item)
            if result is not None:
                return result
    return None

def get_player_stats():
    folder_path = "/mnt/d/Football_data/chelsea_data/data"
    file_path = os.path.join(folder_path, "chelsea_benfica.json")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    player_stats = find_player_stats(data)

    if player_stats is None:
        print("Key playerStats not found")
        return

    player_stats_file = os.path.join(folder_path, "playerStat.json")

    with open(player_stats_file, 'w', encoding='utf-8') as f:
        json.dump(player_stats, f, ensure_ascii=False, indent=4)

    print(f"Saved playerStats to {player_stats_file}")

if __name__ == "__main__":
    get_player_stats()
