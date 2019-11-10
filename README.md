# Optimization for Deep Learning

This repository will contain implementations of popular/recent optimization algorithms for deep learning, including SGD, Adam, AdamW and RAdam. Work in progress!

_____


## Related papers

Material in this repository has been developed as part of a special course / study. This is the tentative list of papers that we discuss:

[An Overview of Gradient Descent Optimization Algorithms](https://arxiv.org/abs/1609.04747)

[On the importance of initialization and momentum in deep learning](https://www.cs.toronto.edu/~fritz/absps/momentum.pdf)

[Aggregated Momentum: Stability Through Passive Damping](https://arxiv.org/abs/1804.00325)

[Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

[On the Convergence of Adam and Beyond](https://arxiv.org/abs/1904.09237)

[Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101)

[On the Variance of the Adaptive Learning Rate and Beyond](https://arxiv.org/abs/1908.03265v1)

[Lookahead Optimizer: k steps forward, 1 step back](https://arxiv.org/abs/1907.08610)

[Adaptive Gradient Methods with Dynamic Bound of Learning Rate](https://arxiv.org/abs/1902.09843)

[On the Convergence of AdaBound and its Connection to SGD](https://arxiv.org/abs/1908.04457v1)

[Why Learning of Large-Scale Neural Networks Behaves Like Convex Optimization](https://arxiv.org/abs/1903.02140v1)

[Optimization Methods for Large-Scale Machine Learning](https://arxiv.org/abs/1606.04838)


## Problem and dataset

For simplicity, we build a small MLP and train it on the MNIST dataset using our own implementations of the optimization algorithms (in PyTorch). In case you somehow stumbled into this repository without ever being exposed to the MNIST dataset, here's a few samples:

![mnist](https://github.com/nicklashansen/neural-net-optimization/blob/master/mnist_examples.png)
