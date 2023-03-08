import random

# Define the rules of the game
success_metric = 100
individual_goal = random.randint(1, 50)
team_goal = success_metric - individual_goal

# Define the matrix
matrix = [
    ["Individual Goal Achieved", "Both Goals Achieved"],
    ["Individual Goal Achieved", "Neither Goal Achieved"]
]

# Define a function to calculate the score for a team member
def calculate_score(focus, success):
    if focus == "individual":
        if success:
            return individual_goal
        else:
            return 0
    elif focus == "team":
        if success:
            return team_goal
        else:
            return 0

# Prompt each team member to choose their focus and calculate their score
team_members = ["Alice", "Bob", "Charlie", "Dave"]
team_scores = {}
for member in team_members:
    focus = input(f"{member}, do you want to focus on your individual goals or the team goals? (individual/team)")
    success = input(f"{member}, did you achieve the success metric? (yes/no)")
    team_scores[member] = calculate_score(focus, success == "yes")

# Calculate the team score
team_score = sum(team_scores.values())

# Evaluate the success of the sprint
if team_score >= success_metric:
    print("The team achieved the success metric!")
else:
    print("The team did not achieve the success metric.")
