import json


def load_best_score():
    try:
        with open("score.json", "r") as file:  # Utilisez "score.json" au lieu de "best_score.json"
            data = json.load(file)
            return data.get("best_score", 0)
    except FileNotFoundError:
        return -1


def update_best_score(new_score):
    best_score = load_best_score()
    if new_score > best_score:
        data = {"best_score": new_score}
        with open("score.json", "w") as file:
            json.dump(data, file)
