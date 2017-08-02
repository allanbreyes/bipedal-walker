Bipedal Walker
==============

by [Allan Reyes](https://allanbreyes.github.io)

## Domain

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
