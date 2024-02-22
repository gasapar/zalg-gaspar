import math


class Vector2d:
    """
    Represents a 2D cartesian vector.
    """
    def __init__(self, x: float = float("nan"), y: float = float("nan")):
        self.x = x
        self.y = y

    def print(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

    def norm(self) -> float:
        """
        Returns the norm of the vector.
        :return: value of the norm
        """
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> None:
        """
        Normalizes the vector, making it have norm equal to one.
        :return: None
        """
        vec_norm = self.norm()
        self.x /= vec_norm
        self.y /= vec_norm

    def multiply(self, value: float):
        """
        Multiplies the vector by the given value and returns new vector.
        :param value: scalar value
        :return: new vector
        """
        x_new = self.x * value
        y_new = self.y * value
        return Vector2d(x_new, y_new)

    def divide(self, value: float):
        """
        Divides the vector by the given value and returns new vector.
        :param value: scala nonzero value
        :return: new vector
        """
        if value == 0.0:
            raise ZeroDivisionError

        return self.multiply(1/value)

    def copy(self):
        """
        Returns a copy of the vector.
        :return: new vector
        """
        return Vector2d(self.x, self.y)
