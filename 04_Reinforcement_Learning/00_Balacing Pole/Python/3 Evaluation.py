import gymnasium as gym
from stable_baselines3 import PPO

# Create our training environment - a cart with a pole that needs balancing
env = gym.make("CartPole-v1", render_mode="human")
model = PPO.load("ppo balancing model", env=env)
for episode in range(1, 11):
    score = 0
    obs, info = env.reset()
    done = False

    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info, whatever = env.step(action)
        score += reward

    print('Episode:', episode, 'Score:', score)
env.close()