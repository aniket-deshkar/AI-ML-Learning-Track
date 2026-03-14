scores ={
    "Amit": 78,
    "Neha": 92,
    "Rohit": 65,
    "Raghac": 45,
    "John":60
}
print("Given data:", scores.items())
increased_scores = {key: value + 5 for key, value in scores.items()}
print("Increased scores by 5:", increased_scores.items())
high_score = {key: value for key, value in scores.items() if value >= 70}
print("High score by 70:", high_score.items())
scores_to_grades = {name :'Grade A' if score >= 80 else 'Grade B' if score >= 60 else 'Grade C' for name, score in scores.items() }
print("Scores to grades:", scores_to_grades.items())