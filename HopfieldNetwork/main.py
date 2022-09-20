
import numpy as np
import random
import time

from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import animation

class Network:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.neurons = np.random.choice([-1, 1], size=(num_neurons,))
        self.weights = np.random.normal(0, 1, size=(num_neurons, num_neurons))

    def set_neurons(self, neurons):
        assert isinstance(neurons, np.ndarray)
        assert neurons.shape == (self.num_neurons,)
        self.neurons = neurons

    def update_neuron(self, idx):
        temp_neurons = self.neurons
        temp_neurons[idx] = np.sign(np.sum(self.weights[idx] * self.neurons))
        self.set_neurons(temp_neurons)

    def update_random_neuron(self):
        self.update_neuron(random.randrange(0, self.num_neurons))
    
    def update_neurons(self, n):
        for _ in range(n):
            self.update_random_neuron()

    def learn_states(self, states):
        outer_products = []
        for state in states:
            assert isinstance(state, np.ndarray)
            assert state.shape == (self.num_neurons,)
            outer_products.append(np.outer(state, state))
        self.weights = np.mean(outer_products, axis=0)
        # set diagonal to 0
        self.weights[np.diag_indices_from(self.weights)] = 0
        
    def learn_state(self, desired_state):
        self.learn_states([desired_state])

def ascii_art_to_state(ascii_art):
    # '.' = -1, '#' = 1
    return np.array([-1 if c == '.' else 1 for c in ascii_art if c in {'.', '#'}])

def animate_convergence(nn_shape, states, im_scale=10, anim_time=None, noise=None):
    fig = plt.figure()

    nn_im_size = (nn_shape[0], nn_shape[1])
    nn_size = nn_im_size[0] * nn_im_size[1]
    upscaled_im_size = (nn_im_size[0] * im_scale, nn_im_size[1] * im_scale)

    nn = Network(nn_size)

    if noise is not None:
        nn.set_neurons(noise.reshape(nn_size))

    nn.learn_states(states)

    im = Image.fromarray(nn.neurons.reshape(nn_im_size).astype(np.uint8) * 255).resize(upscaled_im_size, Image.Resampling.NEAREST)
    pim = plt.imshow(im, cmap='gray')

    def update(i):
        nn.update_neurons(i)
        im = Image.fromarray(nn.neurons.reshape(nn_im_size).astype(np.uint8) * 255).resize(upscaled_im_size, Image.Resampling.NEAREST)
        pim.set_data(im)
        return [pim]

    anim = animation.FuncAnimation(fig, update, interval=1, repeat=False)
    if anim_time is not None:
        plt.show(block=False)
        plt.pause(anim_time)
        plt.close()
    else:
        plt.show()

def main():
    
    states = [
        ascii_art_to_state(  # make concentric squares
        '''
        # # # # # # # #
        # . . . . . . #
        # . # # # # . #
        # . # . . # . #
        # . # . . # . #
        # . # # # # . #
        # . . . . . . #
        # # # # # # # #
        '''),
        ascii_art_to_state(  # make an X
        '''
        # . . . . . . #
        . # . . . . # .
        . . # . . # . .
        . . . # # . . .
        . . . # # . . .
        . . # . . # . .
        . # . . . . # .
        # . . . . . . #
        '''),
        ascii_art_to_state(  # make a circle
        '''
        . . # # # # . .
        . # . . . . # .
        # . . . . . . #
        # . . . . . . #
        # . . . . . . #
        # . . . . . . #
        . # . . . . # .
        . . # # # # . . 
        '''),
        ascii_art_to_state(  # fill the top half with #'s
        '''
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        '''),
        ascii_art_to_state(  # fill the left half with #'s
        '''
        # # # # . . . .
        # # # # . . . .
        # # # # . . . .
        # # # # . . . .
        # # # # . . . .
        # # # # . . . .
        # # # # . . . .
        # # # # . . . .
        ''')
    ]

    for _ in range(10):
        animate_convergence((8, 8), states, anim_time=2)

if __name__ == '__main__':
    main()