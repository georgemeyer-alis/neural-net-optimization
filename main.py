import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
from torch import utils
from torch.nn import Parameter
import misc
import optimizers
from copy import deepcopy

class MLP(nn.Module):
	"""
	A small multilayer perceptron with parameters that we can optimize for the task.
	"""
	def __init__(self, num_features, num_hidden, num_outputs):
		super(MLP, self).__init__()

		self.W_1 = Parameter(init.xavier_normal_(torch.Tensor(num_hidden, num_features)))
		self.b_1 = Parameter(init.constant_(torch.Tensor(num_hidden), 0))

		self.W_2 = Parameter(init.xavier_normal_(torch.Tensor(num_outputs, num_hidden)))
		self.b_2 = Parameter(init.constant_(torch.Tensor(num_outputs), 0))

	def forward(self, x):
		x = F.relu(F.linear(x, self.W_1, self.b_1))
		x = F.linear(x, self.W_2, self.b_2)

		return x


def fit(net, data, optimizer, batch_size=64, num_epochs=250):
	"""
	Fits parameters of a network `net` using `data` as training data and a given `optimizer`.
	"""
	x_train, y_train, x_val, y_val = data

	train_generator = utils.data.DataLoader(misc.Dataset(x_train, y_train), batch_size=batch_size)
	val_generator = utils.data.DataLoader(misc.Dataset(x_val, y_val), batch_size=batch_size)

	losses = misc.AvgLoss()
	val_losses = misc.AvgLoss()

	for epoch in range(num_epochs+1):

		epoch_loss = misc.AvgLoss()
		epoch_val_loss = misc.AvgLoss()

		for x, y in val_generator:
			epoch_val_loss += F.cross_entropy(net(x), y.type(torch.LongTensor))

		for x, y in train_generator:
			loss = F.cross_entropy(net(x), y.type(torch.LongTensor))
			epoch_loss += loss

			optimizer.zero_grad()
			loss.backward()
			optimizer.step()

		if epoch % 10 == 0:
			print(f'Epoch {epoch}/{num_epochs}, loss: {epoch_loss}, val loss: {epoch_val_loss}')

		losses += epoch_loss.losses
		val_losses += epoch_val_loss.avg

	return losses


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-algorithm', type=str, default='SGD')
	args = parser.parse_args()

	data = misc.load_mnist()
	misc.plot_mnist(data[0])
	print(f'Loaded data partitions: ({len(data[0])}, {len(data[2])}, {len(data[4])})')

	net = MLP(num_features=784, num_hidden=64, num_outputs=10)

	sgd_nesterov_net = deepcopy(net)
	sgd_nesterov_opt = optimizers.SGD(
		params=sgd_nesterov_net.parameters(),
		lr=1e-3,
		mu=0.9,
		nesterov=True
	)
	sgd_nesterov_loss = fit(sgd_nesterov_net, data[:4], sgd_nesterov_opt)

	sgd_net = deepcopy(net)
	sgd_opt = optimizers.SGD(
		params=sgd_net.parameters(),
		lr=1e-3
	)
	sgd_loss = fit(sgd_net, data[:4], sgd_opt)

	sgd_momentum_net = deepcopy(net)
	sgd_momentum_opt = optimizers.SGD(
		params=sgd_momentum_net.parameters(),
		lr=1e-3,
		mu=0.9
	)
	sgd_momentum_loss = fit(sgd_momentum_net, data[:4], sgd_momentum_opt)

	misc.plot_losses([sgd_loss, sgd_momentum_loss, sgd_nesterov_loss], labels=['SGD', 'SGD w/ momentum', 'SGD w/ nesterov'], num_epochs=250)
