import random

# Define payoffs
STAG_SUCCESS_PAYOFF = 2
STAG_FAILURE_PAYOFF = 1
HARE_FAILURE_PAYOFF = 0


# Define function to play the game
def play_game(num_team_members):
    # Assign random choices to each team member
    choices = [random.choice(["Stag", "Hare"]) for _ in range(num_team_members)]
    num_stags = choices.count("Stag")

    # Calculate payoff for the team
    if num_stags == num_team_members:
        # All team members hunted stag successfully
        team_payoff = [STAG_SUCCESS_PAYOFF for _ in range(num_team_members)]
    elif num_stags == 0:
        # All team members hunted hare unsuccessfully
        team_payoff = [HARE_FAILURE_PAYOFF for _ in range(num_team_members)]
    else:
        # Some team members hunted stag successfully, others hunted hare unsuccessfully
        team_payoff = [STAG_FAILURE_PAYOFF if choice == "Hare" else HARE_FAILURE_PAYOFF for choice in choices]

    # Print choices and payoff for each team member
    for i, choice in enumerate(choices):
        print(f"Team member {i + 1} chose {choice} and received a payoff of {team_payoff[i]}.")

    # Print total payoff for the team
    total_payoff = sum(team_payoff)
    print(f"The team received a total payoff of {total_payoff}.\n")

    return total_payoff


# Define function to run multiple rounds of the game
def run_game(num_rounds, num_team_members):
    total_team_payoff = 0
    for i in range(num_rounds):
        print(f"Round {i + 1}:")
        round_team_payoff = play_game(num_team_members)
        total_team_payoff += round_team_payoff
    print(f"The team received a total payoff of {total_team_payoff} over {num_rounds} rounds.")


# Example usage
run_game(5, 4)
