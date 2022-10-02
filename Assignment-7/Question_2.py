from typing import List

"""
The Time complexity of this solution is O(1)
As we are only ran loop for 1 time to find out the points
"""
def getDistance(x1,y1,x2,y2,x3,y3):
    # to find the out the area of triangle
    distance = 0.5*(abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))

    return distance


def isCollinear(points:List[List[int]]) -> str:

    result = 0

    # Run the loop only one time i.e i=0 only to find out the all the points
    for i in range(0,1):

        x1,y1 = points[i][0], points[i][1] # x1 = 1, y1=1
        x2,y2 = points[i+1][0], points[i+1][1] # x2 = 1, y2=6
        x3,y3 = points[i+2][0], points[i+2][1] # x3 = 0, y3=9

        result = getDistance(x1,y1,x2,y2,x3,y3)

        # If the area of triangle is 0 then points are collinear else No
        if result == 0:
            return "Yes"

    return "No"


if __name__ == '__main__':

    points = [(1,1), (1,6), (0,9)]

    print(isCollinear(points))