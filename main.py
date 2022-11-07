from matplotlib import pyplot as plt
from collections import Counter


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

if __name__ == '__main__':
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

    plt.bar([x + 5 for x in histogram.keys()],
            histogram.values(),
            10,
            edgecolor=(0,0,0)
    )
    plt.axis([-5, 105, 0, 5])
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel('decile')
    plt.ylabel('no of studets')
    plt.title('dist of exam')
    plt.show()
