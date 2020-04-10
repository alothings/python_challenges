"""

Task: Given 4 points A, B, C, and D. in a 3d system.
angle between plane made by abc and bcd in degrees.
Call angle phi.

cos(phi) = (x.y)/|x||y| where x = ab x bc and y = bc x cd
x.y : dot product
ab x bc: means cross product
ab = b-a

Input: 4 lines, each containing x, y, z values of each point.

Output: angle up to 2 decimal. ie: 8.19

"""
import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        new_x = self.x - no.x
        new_y = self.y - no.y
        new_z = self.z - no.z
        return Points(new_x, new_y, new_z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        s1 = self.y * no.z - self.z * no.y
        s2 = self.z * no.x - self.x * no.z
        s3 = self.x * no.y - self.y * no.x
        return Points(s1, s2, s3)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))