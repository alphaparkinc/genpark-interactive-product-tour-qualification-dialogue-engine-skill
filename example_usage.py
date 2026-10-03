"""Example usage for Product Tour Qualification Dialogue Engine."""
from client import ProductTourDialogueEngine

if __name__ == "__main__":
    resp = {
        "user_role": "VP Product",
        "goal": "improve sales conversion with demo agents",
        "team_size": 25
    }
    path = ProductTourDialogueEngine.compute_tour_path(resp)
    print("Role Profile:", path["qualification_profile"])
    for tr in path["tracks"]:
        print(f"- {tr['module']} ({tr['duration_minutes']} min): {tr['focus']}")
