from heapq import heappush, heappop
import math


def get_distance(x,y):

    return math.sqrt(x**2 + y**2)


def KClosestPoint(points, k):

    N = len(points)
    min_heap,result = [],[]
    for i in range(N):

        x = points[i][0]
        y = points[i][1]

        heappush(min_heap, (get_distance(x,y), points[i]))

    print(min_heap)

    for i in range(k):
        result.append(heappop(min_heap)[1])


    return result


if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    k = 1

    print(f"{k} closest points are : {KClosestPoint(points, k)}")