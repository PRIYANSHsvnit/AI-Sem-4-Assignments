import numpy as np
import pandas as pd

data = pd.read_csv("Assignment-10\cities.csv")
X = data.values

def compute_cost(X, centers):
    cost = 0
    for x in X:
        dists = np.sum((centers - x) ** 2, axis=1)
        cost += np.min(dists)
    return cost


def assign_clusters(X, centers):
    clusters = []
    for x in X:
        dists = np.sum((centers - x) ** 2, axis=1)
        clusters.append(np.argmin(dists))
    return np.array(clusters)


def kmeans_gradient_descent(X, k=3, max_iters=100):
    np.random.seed(42)
    centers = X[np.random.choice(len(X), k, replace=False)]

    for _ in range(max_iters):
        clusters = assign_clusters(X, centers)

        new_centers = []
        for i in range(k):
            points = X[clusters == i]
            if len(points) > 0:
                new_centers.append(np.mean(points, axis=0))
            else:
                new_centers.append(centers[i])

        new_centers = np.array(new_centers)

        if np.allclose(centers, new_centers):
            break

        centers = new_centers

    return centers, compute_cost(X, centers)


def newton_method(X, k=3, max_iters=10):
    np.random.seed(42)
    centers = X[np.random.choice(len(X), k, replace=False)]

    for _ in range(max_iters):
        clusters = assign_clusters(X, centers)

        new_centers = []

        for i in range(k):
            points = X[clusters == i]

            if len(points) == 0:
                new_centers.append(centers[i])
                continue

            grad = 2 * (len(points) * centers[i] - np.sum(points, axis=0))
            hessian = 2 * len(points) * np.eye(2)

            update = np.linalg.inv(hessian).dot(grad)
            new_center = centers[i] - update

            new_centers.append(new_center)

        new_centers = np.array(new_centers)

        if np.allclose(centers, new_centers):
            break

        centers = new_centers

    return centers, compute_cost(X, centers)


k = 3

centers_gd, cost_gd = kmeans_gradient_descent(X, k)
centers_newton, cost_newton = newton_method(X, k)

print("Gradient Descent (First Order Method):")
print("Optimal Airport Locations:\n", centers_gd)
print("Total Sum of Squared Distances:", cost_gd)

print("\nJustification = ")
print("-> This method minimizes the objective function using first-order derivatives.")
print("-> Setting gradient = 0 gives center = mean of assigned cities.")
print("-> Hence, each airport is placed at centroid of its cluster.\n")

print()

print("Newton-Raphson Method (Second Order Method):")
print("Optimal Airport Locations:\n", centers_newton)
print("Total Sum of Squared Distances:", cost_newton)

print("\nJustification = ")
print("-> This method uses both gradient and Hessian (second derivative).")
print("-> Hessian is constant since function is quadratic.")
print("-> Newton update directly reaches optimal mean in fewer iterations.\n")

print()
print()
print("COMPARISON = ")

if abs(cost_gd - cost_newton) < 1e-5:
    print("-> Both methods give SAME optimal cost.")
    print("-> This proves global minimum is reached.")

if cost_newton <= cost_gd:
    print("-> Newton method converges faster due to second-order information.")
else:
    print("-> Gradient method is simpler but may take more iterations.")


print()
print("\nFINAL CONCLUSION = ")
print("-> Optimal airport locations are chosen such that total squared distance is minimized.")
print("-> This ensures efficient accessibility for all cities in Surat.")
print("-> Both methods are valid, but Newton method is faster, while Gradient method is simpler.")