import math
from .base import Coordinate2D, Coordinate3D

class Cartesian2D(Coordinate2D):
    def __init__(self, x, y):
        super().__init__(x, y)

    def to_polar(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return Polar(r, theta)

    def to_cartesian2d(self):
        return self

    def to_cartesian3d(self):
        return Cartesian3D(self.x, self.y, 0)

class Cartesian3D(Coordinate3D):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def to_spherical(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        theta = math.atan2(self.y, self.x)
        phi = math.acos(self.z / r)
        return Spherical(r, theta, phi)

    def to_cartesian2d(self):
        return Cartesian2D(self.x, self.y)

    def to_cartesian3d(self):
        return self


class Polar(Coordinate2D):
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

    def to_cartesian2d(self):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        return Cartesian2D(x, y)

class Spherical(Coordinate3D):
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi

    def to_cartesian3d(self):
        x = self.r * math.sin(self.phi) * math.cos(self.theta)
        y = self.r * math.sin(self.phi) * math.sin(self.theta)
        z = self.r * math.cos(self.phi)
        return Cartesian3D(x, y, z)
