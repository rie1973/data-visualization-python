##Creating plot points for randomwalk.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make random walk, Use while true statement to keep making new walks, as long as program is active

while True:
    #make random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plot point on walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    # colormap to show order or points in walk
    point_numbers =range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
cmap=plt.cm.Blues,
            edgecolors='none', s=15)

    #Mark first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
