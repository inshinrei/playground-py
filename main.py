from liner_algebra.probability import normal_cdf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    xs = [x / 10.0 for x in range(-50, 50)]

    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')

    plt.legend()
    plt.title('Normal CDF')
    plt.show()
