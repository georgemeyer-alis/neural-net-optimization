import os
import pickle as pkl

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import torch
import torchvision
from torch.utils import data
from torchvision import transforms


def load_cifar(num_train=128, num_val=64, batch_size=64):
	"""
	Loads a subset of the CIFAR dataset and returns it as a tuple.
	"""
	transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5),(0.5, 0.5, 0.5))])

	train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
	val_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

	train_dataset, _ = torch.utils.data.random_split(train_dataset, lengths=[num_train, len(train_dataset)-num_train])
	val_dataset, _ = torch.utils.data.random_split(val_dataset, lengths=[num_val, len(val_dataset)-num_val])

	return train_dataset, val_dataset


def load_mnist(filename='data/mnist.npz', num_train=4096, num_val=256, num_test=512):
	"""
	Loads a subset of the grayscale MNIST dataset and returns it as a tuple.
	"""
	data = np.load(filename)

	x_train = data['X_train'][:num_train].astype('float32')
	y_train = data['y_train'][:num_train].astype('int32')

	x_valid = data['X_valid'][:num_val].astype('float32')
	y_valid = data['y_valid'][:num_val].astype('int32')

	x_test = data['X_test'][:num_test].astype('float32')
	y_test = data['y_test'][:num_test].astype('int32')

	return x_train, y_train, x_valid, y_valid, x_test, y_test


class AvgLoss():
	"""
	Utility class that tracks the average loss.
	"""
	def __init__(self):
		self.sum, self.avg, self.n = 0, 0, 0
		self.losses = []

	def __iadd__(self, other):
		try:
			loss = other.data.numpy()
		except:
			loss = other
		
		if isinstance(other, list):
			self.losses.extend(other)
			self.sum += np.sum(other)
			self.n += len(other)
		else:
			self.losses.append(float(loss))
			self.sum += loss
			self.n += 1

		self.avg = self.sum / self.n

		return self

	def __str__(self):
		return '{0:.4f}'.format(round(self.avg, 4))

	def __len__(self):
		return len(self.losses)


class Dataset(data.Dataset):
	def __init__(self, X, y):
		self.X = X
		self.y = y

	def __len__(self):
		return len(self.X)

	def __getitem__(self, idx):
		return self.X[idx], self.y[idx]


def save_losses(losses, filename:str):
	if not os.path.exists('losses/'): os.makedirs('losses/')
	with open(f'losses/{filename}.pkl', 'wb') as f:
		pkl.dump(losses, f, protocol=pkl.HIGHEST_PROTOCOL)


def load_losses(filename:str):
	with open(f'losses/{filename}.pkl', 'rb') as f:
		return pkl.load(f)


def plot_mnist(X):
	idx, dim, classes = 0, 28, 10
	canvas = np.zeros((dim*classes, classes*dim))

	for i in range(classes):
		for j in range(classes):
			canvas[i*dim:(i+1)*dim, j*dim:(j+1)*dim] = X[idx].reshape((dim, dim))
			idx += 1

	sns.set(style='darkgrid')
	plt.figure(figsize=(9, 9))
	plt.axis('off')
	plt.tight_layout(pad=0)
	plt.imshow(canvas, cmap='gray')
	plt.savefig('mnist_examples.png')
	plt.clf()


def plot_loss(losses, val_losses, num_epochs):
	sns.set(style='darkgrid')
	plt.figure(figsize=(12, 6))
	plt.plot(np.linspace(0, num_epochs, num=len(losses)), losses.losses, label='Training loss')
	plt.plot(np.linspace(0, num_epochs, num=len(val_losses)), val_losses.losses, label='Validation loss')
	plt.tight_layout(pad=2)
	plt.xlabel('Epoch')
	plt.ylabel('Negative log likelihood')
	plt.savefig('loss.png')
	plt.clf()


def plot_losses(losses, val_losses, labels, num_epochs, plot_epochs=False):
	sns.set(style='darkgrid')
	plt.figure(figsize=(12, 6))

	colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

	for i in range(len(losses)):
		if plot_epochs:
			epoch_losses = []
			num_batches = len(losses[i].losses) // (num_epochs + 1)
			for j in range(num_epochs + 1):
				epoch_loss = 0
				for k in range(num_batches):
					epoch_loss += losses[i].losses[j * num_batches + k]
				epoch_losses.append(epoch_loss)
			plt.plot(range(num_epochs + 1), epoch_losses, label=labels[i], alpha=0.75)
		else:
			plt.plot(np.linspace(0, num_epochs, num=len(losses[i])), losses[i].losses, label=labels[i], alpha=0.75, c=colors[i])
			plt.plot(np.linspace(0, num_epochs, num=len(val_losses[i])), val_losses[i].losses, alpha=0.75, linestyle='--', c=colors[i])

	plt.tight_layout(pad=2)
	plt.xlabel('Epoch')
	plt.ylabel('Negative log likelihood')
	plt.legend(loc='upper right')
	plt.savefig('loss.png')
	plt.clf()
