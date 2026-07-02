import gymnasium as gym

# Create our training environment - a cart with a pole that needs balancing
env = gym.make("CartPole-v1", render_mode="human")

for episode in range(1, 11):
    score = 0
    state = env.reset()
    done = False

    while not done:
        env.render()

        # Gives two discrete values, 0( or) 1 to move left( or) right.
        # Using sample() will return a random number, either 0( or) 1.

        action = env.action_space.sample()
        n_state, reward, done, info, logger = env.step(action)
        score += reward

    print('Episode:', episode, 'Score:', score, 'State:' , n_state)
env.close()
