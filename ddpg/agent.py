from ostruct import OpenStruct

from actor_critic import Actor, Critic
from memory import Memory

# FIXME
import gym


class Agent:
    def __init__(
        self, name, env,

        # Configuration
        load=False,

        # Q-learning hyperparameters
        gamma=0.99,

        # ANN hyperparameters
        alpha_actor=0.0001,
        alpha_critic=0.001,
        hidden_layers=[400, 300],

        # Experience replay hyperparameters
        memory_max=2**16,
        memory_min=2**6,
        batch_size=2**5
    ):
        self.name = name
        self.env  = env

        self.memory = Memory(
            minlen=memory_min, maxlen=memory_max,
            batch_size=batch_size, validator=self.validate_experience)

        self.create_actor(alpha=alpha_actor, hidden_layers=hidden_layers)
        self.create_critic(alpha=alpha_critic, hidden_layers=hidden_layers)

    def create_actor(self, alpha, hidden_layers):
        params = {
            'input_shape':      self.env.observation_space.shape,
            'output_shape':     self.env.action_space.shape,
            'hidden_layers':    hidden_layers
        }
        self.actor = OpenStruct()
        self.actor.online = Actor("{}.actor.online".format(self.name), **params)
        self.actor.target = Actor("{}.actor.target".format(self.name), **params)

    def create_critic(self, alpha, hidden_layers):
        params = {
            'input_shape':      self.env.observation_space.shape,
            'output_shape':     self.env.action_space.shape,
            'hidden_layers':    hidden_layers
        }
        self.critic = OpenStruct()
        self.critic.online = Critic("{}.critic.online".format(self.name), **params)
        self.critic.target = Critic("{}.critic.target".format(self.name), **params)

    def validate_experience(self, experience):
        # Expected: [s, a, r, s', done]
        return experience.shape == (5,)


if __name__ == '__main__':
    env = gym.make('BipedalWalker-v2')
    agent = Agent('ddpg', env)
