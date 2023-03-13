import numpy as np

# Define the number of team members and tasks
num_team_members = 4
num_tasks = 6

# Initialize the values for each task
task_values = np.array([50, 40, 60, 35, 45, 55])

# Initialize the values for each team member's contribution to each task
member_task_contributions = np.array([[20, 5, 15, 10, 0, 0],
                                      [5, 20, 5, 0, 5, 0],
                                      [10, 5, 20, 0, 10, 5],
                                      [15, 5, 15, 5, 5, 10]])

# Calculate the total value of completed work for each possible combination of team members
total_values = []
for i in range(2**num_team_members):
    binary = format(i, f'0{num_team_members}b')
    team_members = np.array([int(b) for b in binary])
    team_value = np.sum(np.max(member_task_contributions[:,team_members], axis=1) * task_values)
    total_values.append((team_members, team_value))

# Calculate the Shapley value for each team member
shapley_values = np.zeros(num_team_members)
for i in range(num_team_members):
    for j in range(2**num_team_members):
        binary = format(j, f'0{num_team_members}b')
        team_members = np.array([int(b) for b in binary])
        if team_members[i] == 0:
            coalition_value_1 = 0
            coalition_value_2 = 0
            for k in range(len(total_values)):
                if np.array_equal(team_members + np.eye(num_team_members)[i], total_values[k][0]):
                    coalition_value_1 = total_values[k][1]
                elif np.array_equal(team_members, total_values[k][0]):
                    coalition_value_2 = total_values[k][1]
            shapley_values[i] += (coalition_value_1 - coalition_value_2) / (2**num_team_members)

# Print the total value of completed work for each possible combination of team members
for team in total_values:
    print(f'Team Members: {team[0]}, Total Value: {team[1]}')

# Print the Shapley value for each team member
for i in range(num_team_members):
    print(f'Team Member {i+1} Shapley Value: {shapley_values[i]}')
