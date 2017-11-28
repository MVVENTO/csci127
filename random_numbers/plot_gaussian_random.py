import matplotlib.pyplot as plt
import numpy as np
def generate_gaussian_random(n,mu, sigma ,plot=True):
    a= np.random.normal(mu, sigma ,n)
    hist, bin_edges = np.histogram(a , density=True)
    if plot:
        count, bins, ignored = plt.hist(a, 100, normed=True)
        plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
 linewidth=2, color='r')
        plt.title("when n="+str(n))
        plt.show()
        plt.close()

if __name__ == '__main__':
    (mu, sigma)=(0,  0.1)
    for n in range(1000,300000,10000):
        generate_gaussian_random(n,mu, sigma)
