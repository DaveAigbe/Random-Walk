import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # starting position
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # ending position

    # plt.savefig('Random Walk Visual 7', bbox_inches='tight')
    plt.show()

    keep_running = input("Create another plot? (Y/N): ").lower()
    if keep_running == 'n':
        break
