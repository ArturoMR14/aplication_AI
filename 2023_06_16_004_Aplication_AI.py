import gym
from stable_baselines3 import PPO

env = gym.make('LunarLander-v2') 
env.reset()

model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

episodes = 10

for ep in range(episodes):
	obs = env.reset()
	done = False
	while not done:
		action, _states = model.predict(obs)
		obs, rewards, done, info = env.step(action)
		env.render()
		print(rewards)
	