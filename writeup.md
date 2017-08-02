Bipedal Walker
==============

by [Allan Reyes](https://allanbreyes.github.io)

## Domain

Several recent advancements in **Reinforcement Learning** have proven
tremendously successful in scaling learning architectures beyond simple grid
games to problems of increasing complexity. While obstacles in extending
reinforcement learning broadly to real-world applications are enumerable, the
focus of this study is on addressing the challenges associated with high
dimensionality and continuous ranges of both state and action spaces.

Previous work has been conducted to use Deep Q-Networks (**DQN**) as function
approximators to address state space complexity ([Mnih 2013][5]; [Mnih 2015][4])
and Deep Deterministic Policy Gradients (**DDPG**) to address action state space
complexity ([Silver 2014][7]; [Lillicrap 2016][3]). Lastly, evolutionary
algorithms have showed extraordinary promise as alternatives to traditional
reinforcement learning paradigms ([Salimans 2017][6]). While previous studies
have empirically demonstrated generality of these new approaches, the scope of
this study attempts to synthesize, optimize, and compare these algorithms
against a single, common problem: control of a bipedal walker, using [OpenAI's
BipedalWalker-v2][BipedalWalker-v2] environment.

This study is of particular interest for two reasons. First, the control problem
itself is non-trivial due to the space complexity. And secondly, a successful
reproduction strengthens the applicability of prior research.

## Model

> Reward is given for moving forward, total 300+ points up to the far end. If
the robot falls, it gets -100. Applying motor torque costs a small amount of
points, more optimal agent will get better score. State consists of hull angle
speed, angular velocity, horizontal speed, vertical speed, position of joints
and joints angular speed, legs contact with ground, and 10 LIDAR rangefinder
measurements. There's no coordinates in the state vector.

## Algorithm

## Benchmarks

## Evaluation Metrics

## Project Design

## References

### Libraries and Websites

[Keras][Keras]

[OpenAI Gym, BipedalWalker-v2][BipedalWalker-v2]

### Papers

[Ioffe, S., & Szegedy, C. (2015). Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. Arxiv, 1–11.][1]

[Konda, V. R., & Tsitsiklis, J. N. (2000). Actor-Critic Algorithms. Nips.][2]

[Lillicrap, T. P., Hunt, J. J., Pritzel, A., Hess, N., Erez, T., Tassa, Y., … Wierstra, D. (2016). Continuous control with deep reinforcement learning. Foundations and Trends® in Machine Learning, 2][3]

[Mnih, V. et al. (2015). Human-level control through deep reinforcement learning. Nature.][4]

[Mnih, V., Silver, D., & Riedmiller, M. (2013). Playing Atari with Deep Reinforcement Learning, 1–9.][5]

[Salimans, T., Ho, J., Chen, X., & Sutskever, I. (2017). Evolution Strategies as a Scalable Alternative to Reinforcement Learning, 1–13.][6]

[Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., & Riedmiller, M. (2014). Deterministic Policy Gradient Algorithms. Proceedings of the 31st International Conference on Machine Learning (ICML-14), 387–395.][7]

<!-- Links -->
[Keras]: https://github.com/fchollet/keras
[BipedalWalker-v2]: https://gym.openai.com/envs/BipedalWalker-v2

[1]: https://arxiv.org/abs/1502.03167
[2]: http://web.mit.edu/jnt/www/Papers/J094-03-kon-actors.pdf
[3]: https://arxiv.org/pdf/1509.02971.pdf
[4]: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf
[5]: https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
[6]: https://arxiv.org/pdf/1703.03864.pdf
[7]: http://proceedings.mlr.press/v32/silver14.pdf
