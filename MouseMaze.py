# 3x2 maze
import random

class MouseMaze:
    def __init__(self):
        self.maze = [
            [0], [1], [0],
            [0], [-10], [10]
        ]
        self.Q_Table = [[0 for _ in range(4)] for _ in range(6)]  # 6 positions x 4 actions
        self.moveCounter = 0
        self.positionX = 0
        self.positionY = 0
        self.alpha = 0.1
        self.gamma = 0.99
        self.epsilon = 0.1  # exploration rate

    def reset(self):
        self.positionX = 0
        self.positionY = 0
        self.moveCounter = 0
        return self.get_state()

    def get_state(self):
        return self.positionY * 3 + self.positionX

    def move(self, action):
        # 0: Left, 1: Right, 2: Up, 3: Down
        if action == 0 and self.positionX > 0:
            self.positionX -= 1
        elif action == 1 and self.positionX < 2:
            self.positionX += 1
        elif action == 2 and self.positionY < 1:
            self.positionY += 1
        elif action == 3 and self.positionY > 0:
            self.positionY -= 1
        self.moveCounter += 1

    def get_reward(self):
        index = self.get_state()
        return self.maze[index][0]

    def is_terminal(self):
        # Terminal if cheese or poison
        reward = self.get_reward()
        return reward == 10 or reward == -10

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        else:
            return self.Q_Table[state].index(max(self.Q_Table[state]))

    def q_learning(self, episodes=1000):
        for _ in range(episodes):
            state = self.reset()
            while not self.is_terminal():
                action = self.choose_action(state)
                prev_state = state
                self.move(action)
                state = self.get_state()
                reward = self.get_reward()
                best_next = max(self.Q_Table[state])
                # Q-learning update
                self.Q_Table[prev_state][action] += self.alpha * (reward + self.gamma * best_next - self.Q_Table[prev_state][action])
                if self.is_terminal():
                    break

maze_game = MouseMaze()
maze_game.q_learning(episodes=500)


for i, row in enumerate(maze_game.Q_Table):
    print(f"Position {i}:")
    for action, value in enumerate(row):
        print(f"  Action {action}: {value}")
    print("-" * 20) 