'''
35.Given an array of points where points[i] = [xi, yi] represents a 
point on the X-Y plane and an integer k, return the k closest
points to the origin (0, 0).
(i)Input : points = [[1,3],[-2,2],[5,8],[0,1]],k=2
    Output:[[-2, 2], [0, 1]]
(i)Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
(i)Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]

'''
import heapq

def k_closest(points, k):
    # Calculate the squared distance and use a min-heap to find the k closest points
    return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)

# Example usage
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
closest_points = k_closest(points, k)
print(closest_points)  # Output: [[-2, 2], [0, 1]]
