from collections import defaultdict
from random import uniform
from math import sqrt
import math, itertools

dataset = []
with open('data.txt', 'r') as data:
    lines = data.read().splitlines()
    for line in lines[1:]:
        item = [int(i.strip()) for i in line.split(',')]
        dataset.append(item)

colors = ['red', 'blue', 'orange', 'gray', 'purple']


def point_avg(points):
    # Accepts a list of points, each with the same number of dimensions.NB. points can have more dimensions than 2
    # Returns a new point which is the center of all the points.

    dimensions = len(points[0])

    new_center = []

    for dimension in xrange(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center


def update_centers(data_set, assignments):
    # Accepts a dataset and a list of assignments; the indexes of both lists correspond to each other.
    # Compute the center for each of the assigned groups. Return `k` centers where `k` is the number of unique assignments.

    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)

    for points in new_means.itervalues():
        centers.append(point_avg(points))

    return centers


def assign_points(data_points, centers):
    # Given a data set and a list of points betweeen other points,assign each point to an index that corresponds to
    # the index of the center point on it's proximity to that point.

    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in xrange(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def euclidean_distance(a, b):
    e_distance = 0.0
    for i in range(len(a) - 1):
        e_distance += pow((a[i] - b[i]) ** 2)
    return math.sqrt(e_distance)


def update_centers(data_set, assignments):
    # Accepts a dataset and a list of assignments; the indexes of both lists correspond to each other.

    # Compute the center for each of the assigned groups.Return `k` centers where `k` is the number of unique assignments.

    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)

    for points in new_means.itervalues():
        centers.append(point_avg(points))

    return centers


def assign_points(data_points, centers):
    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in xrange(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def k_means(dataset, k):
    center = initialize_centroids(dataset, k)
    assignments = assign_points(dataset, center)
    old_assignments = None
    final_centers = []
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)

    return assignments


def f_coordinate(dataset):
    x = []
    y = []
    for i in dataset:
        x.append(i[0][0])
        y.append(i[0][1])
    return [x, y]


if "__main__" == __name__:

    while True:
        k = int(input("k-value (1-10): "))
        if 1 <= k <= 10:
            break
        else:
            print("Try again!")

    f = plt.figure()
    assignments = k_means(dataset, k)

    result = []
    for i, j in zip(dataset, assignments):
        result.append((i, j))

    result = sorted(result, key=lambda x: x[1])
    L = [list(v) for k, v in itertools.groupby(result, lambda x: x[1])]

    for i, color in zip(L, colors):
        x = find_coordinate_values(i)[0]
        y = find_coordinate_values(i)[1]
        plt.scatter(x, y, label="Cluster " + str(colors.index(color)), color=color,
                    marker=".", s=30)

    plt.xlabel('Income')
    plt.ylabel('Spend')
    plt.legend()
    plt.show()
    f.savefig("plot.pdf", bbox_inches='tight')

