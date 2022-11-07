from matplotlib import pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

if __name__ == '__main__':
    plt.bar(range(len(movies)), num_oscars)
    plt.title('Movies')
    plt.ylabel('# of academy awards')
    plt.xticks(range(len(movies)), movies)
    plt.show()
