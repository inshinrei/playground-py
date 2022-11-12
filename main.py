from matplotlib import pyplot as plt
from collections import Counter


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
mentions = [500, 505]
years = [2017, 2018]
variance     = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error  = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]


if __name__ == '__main__':
    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')

    plt.legend(loc=9)
    plt.xlabel('model complexity')
    plt.xticks([])
    plt.title('bias var')

    plt.show()
