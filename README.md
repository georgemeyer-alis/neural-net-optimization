# Optimization for Deep Learning

This repository contains a benchmark and PyTorch implementations of popular/recent optimization algorithms for deep learning, including SGD, SGD w/ momentum, NSGD, SGDW, RMSProp, Adam, Nadam, AdamW, RAdam and RAdamW. Work in progress!

_____


## Related papers

Material in this repository has been developed as part of a special course / study. This is the tentative list of papers that we discuss:

[An Overview of Gradient Descent Optimization Algorithms](https://arxiv.org/abs/1609.04747)

[Optimization Methods for Large-Scale Machine Learning](https://arxiv.org/abs/1606.04838)

[On the importance of initialization and momentum in deep learning](https://www.cs.toronto.edu/~fritz/absps/momentum.pdf)

[Aggregated Momentum: Stability Through Passive Damping](https://arxiv.org/abs/1804.00325)

[ADADELTA: An Adaptive Learning Rate Method](https://arxiv.org/abs/1212.5701)

[RMSprop](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)

[Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

[On the Convergence of Adam and Beyond](https://arxiv.org/abs/1904.09237)

[Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101)

[On the Variance of the Adaptive Learning Rate and Beyond](https://arxiv.org/abs/1908.03265v1)

[Incorporating Nesterov Momentum Into Adam](https://openreview.net/pdf?id=OM0jvwB8jIp57ZJjtNEZ)

[Adaptive Gradient Methods with Dynamic Bound of Learning Rate](https://arxiv.org/abs/1902.09843)

[On the Convergence of AdaBound and its Connection to SGD](https://arxiv.org/abs/1908.04457v1)

[Lookahead Optimizer: k steps forward, 1 step back](https://arxiv.org/abs/1907.08610)

[The Marginal Value of Adaptive Gradient Methods in Machine Learning](https://arxiv.org/abs/1705.08292)

[Why Learning of Large-Scale Neural Networks Behaves Like Convex Optimization](https://arxiv.org/abs/1903.02140v1)

[Learning Rate Dropout](https://arxiv.org/abs/1912.00144)


_____


## How to run

You can run the experiments and algorithms by calling e.g.

```python main.py -num_epochs 300 -dataset cifar -num_train 32768 ```

with arguments as specified in the file. The algorithms can be run on two different datasets, MNIST and CIFAR-10. For MNIST a small MLP is used for proof of concept, whereas a CNN is used for CIFAR-10. You may optionally decrease the size of the dataset to decrease computational complexity.

_____


## Results

This is the interesting part. Coming soon!
