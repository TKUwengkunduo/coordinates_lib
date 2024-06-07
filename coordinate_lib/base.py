class Coordinate:
    """
    Base class for all coordinate systems.
    """
    def to_cartesian2d(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def to_cartesian3d(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def to_polar(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def to_spherical(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Coordinate2D(Coordinate):
    """
    Base class for 2D coordinate systems.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinate2D(x={self.x}, y={self.y})"

    def to_cartesian2d(self):
        return self

    def to_cartesian3d(self):
        return Coordinate3D(self.x, self.y, 0)


class Coordinate3D(Coordinate):
    """
    Base class for 3D coordinate systems.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Coordinate3D(x={self.x}, y={self.y}, z={self.z})"

    def to_cartesian2d(self):
        return Coordinate2D(self.x, self.y)

    def to_cartesian3d(self):
        return self
