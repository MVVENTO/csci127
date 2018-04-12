import random
import matplotlib.pyplot as plt

#generate N days stock prices based on a random walk pattern.
# random number >0.5     :    up
# random number <=0.5  :   down
def get_prices(N=1000):
    prices = [0]
    for i in range(1,N):
        if random.random()>0.5:
            prices.append(prices[-1]+1)
        else:
            prices.append(prices[-1]-1)
    return prices

if __name__ == "__main__":
    for i in range(2000):
        N = 1000
        prices = get_prices(N)
        plt.plot(range(N),prices)
    plt.show()
            
