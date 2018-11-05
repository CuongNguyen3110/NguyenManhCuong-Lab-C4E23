from matplotlib import pyplot

machines_counts = [18, 4, 2]

machines_names = ["PC", "Mac", "Linux"]
pyplot.pie(machines_counts, labels=machines_names)
pyplot.show()