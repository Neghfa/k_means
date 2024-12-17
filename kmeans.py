import random
import pprint

k = int(input("Please enter the number of centroids: "))
accuracy = 1e-5

lines = []
with open("thepoints.txt") as f:
    for line in f:
        try:
            points = [float(x) for x in line.split(",")]
            if len(points) == 3:
                lines.append(tuple(points))
        except ValueError:
            continue

#random.seed(42)

def calc_distance(point1, point2):
    '''
    Calculates the distance between two 3D points.

    Args:
    - point1 (Tuple): The first point.
    - point2 (Tuple): The second point.

    Returns:
    - res (Float): The distance between point1 and point2
    '''
    
    res = ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2) ** (0.5)
    return res

def assign_point_to_centroid(points, centroids, centroids_list):
    '''
    Assigns each point to the nearest centroid.

    Args:
    - points (List): The list of 3d points.
    - centroids (Dictionary): The dictionary of centroids and empty lists as values.
    - centroids_list (List): The list of centroids.

    Returns:
    - centroids (Dictionary): The dictionary of centroids and nearest points as values.
    '''

    for point in points:
        index, min_distance = 0, calc_distance(point, centroids_list[0])
        for i in range(len(centroids_list)):
            if calc_distance(point, centroids_list[i]) < min_distance:
                index, min_distance = i, calc_distance(point, centroids_list[i])
        centroids[centroids_list[index]].append(point)
    return centroids

def new_clusters(centroids, centroids_list):
    '''
    Creates new centroids based on the mean of the values.

    Args:
    - centroids (Dictionary): The dictionary of centroids and nearest points as values.
    - centroids_list (List): The list of centroids.

    Returns:
    - new_centroids (Dictionary): The dictionary of centroids and empty lists as values.
    - new_centroids_list (List): The list of new centroids calculated by the mean of values.
    '''

    new_centroids_list = []
    x, y, z = 0, 0, 0
    for centroid in centroids_list:            
        for point in centroids[centroid]:
            x += point[0]
            y += point[1]
            z += point[2]
        x /= len(centroids[centroid])
        y /= len(centroids[centroid])
        z /= len(centroids[centroid])
        new_centroids_list.append(tuple((round(x,2), round(y,2), round(z,2))))
    new_centroids = {point: [] for point in new_centroids_list}
    return new_centroids, new_centroids_list

def convergence_check(centroids_list, new_centroids_list, accuracy):
    '''
    Checks if the new centroids are converged by the accuracy mentioned.

    Args:
    - centroids_list (List): The list of centroids.
    - new_centroids_list (List): The list of new centroids.
    - accuracy (Int): The accuracy which the convergence is being checked.

    Returns:
     - True or False (Boolean)
    '''

    for i in range(k):
        dist = calc_distance(centroids_list[i], new_centroids_list[i])
        if dist > accuracy:
            return False
    return True

def kmeans(k,points):
    '''
    Makes k clusters based on distance.

    Args:
    - k (Int): The number of centroids (or clusters).
    - points (List): The list points.

    Returns:
    - centroids (Dictionary): The centroids made.
    - centroids_list (List):
    '''

    # Choosing k random points from the dataset.
    centroids_list = random.sample(points,k)
    print("The first set of centroids are randomly chosen. This is the list of centroids:")
    print(centroids_list)
    centroids = {point: [] for point in centroids_list}
    while True:
        # Assigning points to each centroid.
        centroids = assign_point_to_centroid(points, centroids, centroids_list)
        print("These are the centroids and assigned points.")
        pprint.pprint(centroids, compact=True)
        
        # Creating new clusters based on the mean of each centroids values.
        new_centroids, new_centroids_list = new_clusters(centroids, centroids_list)
        print("New centroids with the mean values of each centroid are made.")

        # Checking if the new centroids are converged or not.
        if convergence_check(centroids_list, new_centroids_list, accuracy):
            print("The new centroids are converged with", accuracy, "accuracy.")
            # Assigning points to each converged centroid. 
            new_centroids = assign_point_to_centroid(points, new_centroids, new_centroids_list)
            print("These are the clusters made from the mean of previous centroids values.")
            pprint.pprint(new_centroids, compact=True)
            break
        else:
            print("The new centroids are not yet converged, So we have to re-Do the proccess.")
        centroids_list = new_centroids_list
        centroids = new_centroids
    return centroids, centroids_list

kmeans(k,lines)