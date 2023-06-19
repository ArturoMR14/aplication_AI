
import gymnasium as gym

 
# create environment
env=gym.make('LunarLander-v2',render_mode='human')

(state,_)=env.reset()



for step in range(200):
	env.render()
	# take random action
	env.step(env.action_space.sample())

env.close()