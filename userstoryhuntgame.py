import random

class Developer:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def estimate(self):
        # In a real scenario, developers will provide their estimates.
        # Here it's random for demonstration purposes.
        return random.choice(["accurate", "inaccurate"])

class Task:
    def __init__(self):
        self.time_required = random.randint(1, 10)  # for demonstration purposes

class Game:
    def __init__(self, developers):
        self.developers = developers

    def play_round(self, task):
        estimates = {dev.name: dev.estimate() for dev in self.developers}
        for dev in self.developers:
            if estimates[dev.name] == "accurate":
                dev.score += 5 if all(est == "accurate" for est in estimates.values()) else 2
            else:  # inaccurate estimate
                dev.score += 3 if any(est == "accurate" for est in estimates.values()) else 0

    def display_scores(self):
        for dev in self.developers:
            print(f"{dev.name}'s score: {dev.score}")

game = Game([Developer('Alice'), Developer('Bob'), Developer('Charlie')])
for _ in range(10):
    task = Task()
    game.play_round(task)
game.display_scores()
