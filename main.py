from matplotlib import pyplot as plt


years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

if __name__ == '__main__':
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    plt.title('nominal GDP')
    plt.ylabel('$')
    plt.show()
