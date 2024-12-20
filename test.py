import numpy as np
from env import Env
from stable_baselines3 import DQN

env = Env(8, 10, False)
model = DQN("MlpPolicy", env)
model = model.load("DQN.zip")

games = 1000
won = 0
for i in range(games):
    obs, _ = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)
        obs = np.array(obs)
        obs, reward, done, _, info = env.step(action)
        if reward == 10:
            won += 1

    print(f"Games played: {i + 1}, Wins: {won}, Win rate: {won / (i + 1):.2f}")

print(f"Total games: {games}, Total wins: {won}, Win rate: {won / games:.2f}")
