import gymnasium as gym
from stable_baselines3 import PPO

# Create our training environment - a cart with a pole that needs balancing
env = gym.make("CartPole-v1", render_mode="human")

model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=20000)

# save the model
model.save('ppo balancing model')