from matplotlib import pyplot as plt
from collections import Counter


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
mentions = [500, 505]
years = [2017, 2018]

if __name__ == '__main__':
    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel('# of times')
    plt.ticklabel_format(useOffset=False)

    plt.axis([2016.5, 2018.5, 0, 550])
    plt.title('tt')

    plt.show()
