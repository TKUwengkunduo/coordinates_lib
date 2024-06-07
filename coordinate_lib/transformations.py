import math
from .cartesian import Cartesian2D, Cartesian3D
from .base import Coordinate2D, Coordinate3D

class Polar(Coordinate2D):
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

    def to_cartesian2d(self):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        return Cartesian2D(x, y)

    def to_polar(self):
        return self

    def to_cartesian3d(self):
        return Cartesian3D(self.r * math.cos(self.theta), self.r * math.sin(self.theta), 0)

    def to_spherical(self):
        raise NotImplementedError("Polar to Spherical conversion is not defined")

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

    def to_spherical(self):
        return self

    def to_cartesian2d(self):
        raise NotImplementedError("Spherical to Cartesian2D conversion is not defined")

    def to_polar(self):
        raise NotImplementedError("Spherical to Polar conversion is not defined")

# Conversion functions
def to_cartesian2d(coord):
    if isinstance(coord, Coordinate2D):
        return coord.to_cartesian2d()
    elif isinstance(coord, Polar):
        return coord.to_cartesian2d()
    else:
        raise TypeError("Unsupported coordinate type for 2D Cartesian conversion")

def to_cartesian3d(coord):
    if isinstance(coord, Coordinate3D):
        return coord.to_cartesian3d()
    elif isinstance(coord, Spherical):
        return coord.to_cartesian3d()
    else:
        raise TypeError("Unsupported coordinate type for 3D Cartesian conversion")

def to_polar(coord):
    if isinstance(coord, Cartesian2D):
        r = math.sqrt(coord.x ** 2 + coord.y ** 2)
        theta = math.atan2(coord.y, coord.x)
        return Polar(r, theta)
    else:
        raise TypeError("Unsupported coordinate type for Polar conversion")

def to_spherical(coord):
    if isinstance(coord, Cartesian3D):
        r = math.sqrt(coord.x ** 2 + coord.y ** 2 + coord.z ** 2)
        theta = math.atan2(coord.y, coord.x)
        phi = math.acos(coord.z / r)
        return Spherical(r, theta, phi)
    else:
        raise TypeError("Unsupported coordinate type for Spherical conversion")
