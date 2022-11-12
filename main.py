from matplotlib import pyplot as plt
from collections import Counter


friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


if __name__ == '__main__':
    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords="offset")

    plt.title('daily')
    plt.xlabel('#')
    plt.ylabel('spent')

    plt.show()
