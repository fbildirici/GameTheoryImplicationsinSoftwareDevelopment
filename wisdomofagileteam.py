import random
import statistics

class Developer:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def estimate(self):
        # In a real scenario, developers will provide their estimates.
        # Here it's random for demonstration purposes.
        return random.randint(1, 10)

class Task:
    def __init__(self):
        self.actual_effort = random.randint(1, 10)  # for demonstration purposes

class Game:
    def __init__(self, developers):
        self.developers = developers

    def play_round(self, task):
        estimates = {dev: dev.estimate() for dev in self.developers}
        median_estimate = statistics.median(estimates.values())

        for dev, estimate in estimates.items():
            if abs(estimate - task.actual_effort) <= 0.1 * task.actual_effort:
                dev.score += 3 if abs(estimate - task.actual_effort) != 0 else 5

    def display_scores(self):
        for dev in self.developers:
            print(f"{dev.name}'s score: {dev.score}")

game = Game([Developer('Fatih'), Developer('Bebop'), Developer('Donatello')])
for _ in range(10):
    task = Task()
    game.play_round(task)
game.display_scores()
