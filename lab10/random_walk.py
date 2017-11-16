# this is a random walk simulation code
# by jimmy shen Nov 6, 2017
import numpy as np
import matplotlib.pyplot as plt

def random_walk(path_number, moving_steps):
    random_numbers = np.random.rand(path_number, moving_steps)
    random_walks = np.zeros((path_number, moving_steps),dtype=np.float)
    for i in range(path_number):
        for j in range(1,moving_steps):
            if random_numbers[i,j]<=0.5:
                random_walks[i,j]=random_walks[i,j-1]-1
            else:
                random_walks[i,j]=random_walks[i,j-1]+1
    return random_walks

def plot(a):
    for i in range(a.shape[0]):
        plt.scatter(np.arange(a.shape[1]),a[i],alpha=0.3)
        plt.plot(np.arange(a.shape[1]),a[i])
    plt.show()


if __name__=="__main__":

    random_walks=random_walk(1000,2000)
    plot(random_walks)
