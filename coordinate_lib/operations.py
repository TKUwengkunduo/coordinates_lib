import math
from .cartesian import Cartesian2D, Cartesian3D

def translate(point, tx, ty, tz=0):
    if isinstance(point, Cartesian2D):
        return Cartesian2D(point.x + tx, point.y + ty)
    elif isinstance(point, Cartesian3D):
        return Cartesian3D(point.x + tx, point.y + ty, point.z + tz)
    else:
        raise TypeError("Unsupported coordinate type for translation")

def rotate(point, angle, axis=None):
    if isinstance(point, Cartesian2D):
        x_new = point.x * math.cos(angle) - point.y * math.sin(angle)
        y_new = point.x * math.sin(angle) + point.y * math.cos(angle)
        return Cartesian2D(x_new, y_new)
    elif isinstance(point, Cartesian3D):
        if axis == 'x':
            y_new = point.y * math.cos(angle) - point.z * math.sin(angle)
            z_new = point.y * math.sin(angle) + point.z * math.cos(angle)
            return Cartesian3D(point.x, y_new, z_new)
        elif axis == 'y':
            x_new = point.x * math.cos(angle) + point.z * math.sin(angle)
            z_new = -point.x * math.sin(angle) + point.z * math.cos(angle)
            return Cartesian3D(x_new, point.y, z_new)
        elif axis == 'z':
            x_new = point.x * math.cos(angle) - point.y * math.sin(angle)
            y_new = point.x * math.sin(angle) + point.y * math.cos(angle)
            return Cartesian3D(x_new, y_new, point.z)
        else:
            raise ValueError("Invalid rotation axis for 3D rotation")
    else:
        raise TypeError("Unsupported coordinate type for rotation")

def scale(point, sx, sy, sz=1):
    if isinstance(point, Cartesian2D):
        return Cartesian2D(point.x * sx, point.y * sy)
    elif isinstance(point, Cartesian3D):
        return Cartesian3D(point.x * sx, point.y * sy, point.z * sz)
    else:
        raise TypeError("Unsupported coordinate type for scaling")

def reflect(point, axis):
    if isinstance(point, Cartesian2D):
        if axis == 'x':
            return Cartesian2D(point.x, -point.y)
        elif axis == 'y':
            return Cartesian2D(-point.x, point.y)
        else:
            raise ValueError("Invalid reflection axis for 2D reflection")
    elif isinstance(point, Cartesian3D):
        if axis == 'xy':
            return Cartesian3D(point.x, point.y, -point.z)
        elif axis == 'xz':
            return Cartesian3D(point.x, -point.y, point.z)
        elif axis == 'yz':
            return Cartesian3D(-point.x, point.y, point.z)
        else:
            raise ValueError("Invalid reflection axis for 3D reflection")
    else:
        raise TypeError("Unsupported coordinate type for reflection")

def shear(point, kx=0, ky=0, kz=0):
    if isinstance(point, Cartesian2D):
        x_new = point.x + kx * point.y
        y_new = point.y + ky * point.x
        return Cartesian2D(x_new, y_new)
    elif isinstance(point, Cartesian3D):
        x_new = point.x + kx * point.y + ky * point.z
        y_new = point.y + ky * point.x + kz * point.z
        z_new = point.z + kz * point.x + kx * point.y
        return Cartesian3D(x_new, y_new, z_new)
    else:
        raise TypeError("Unsupported coordinate type for shearing")
