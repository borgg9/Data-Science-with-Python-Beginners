from matplotlib import pyplot as plt
movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West side story']
num_oscars = [5, 11, 3, 8, 10]
xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel('# of Academy Awards')
plt.title('My favourite movies')
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
plt.show()