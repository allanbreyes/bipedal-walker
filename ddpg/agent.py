from memory import Memory


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

    def validate_experience(self, experience):
        # Expected: [s, a, r, s', done]
        return experience.shape == (5,)
