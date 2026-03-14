mlb_teams = {
    "Colorado": "Rockies",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Seattle": "Mariners",
    "Detroit": "Tigers"
}

inverted_teams = { teams : state for teams,state in mlb_teams.items() }
print("Inverted Teams: ",inverted_teams)