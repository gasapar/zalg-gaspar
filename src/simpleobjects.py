import math


class Vector2d:
    """
    Represents a 2D cartesian vector.
    """
    def __init__(self, x: float = float("nan"), y: float = float("nan")):
        self.x: float = x
        self.y: float = y

    def to_string(self) -> str:
        """
        Returns a string representation of the vector.
        @return: text representation of the vector
        """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def print(self) -> None:
        """
        Prints the vector to the console window.
        @return: None
        """
        print(self.to_string())

    def norm(self) -> float:
        """
        Returns the norm of the vector.
        @return: value of the norm
        """
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> None:
        """
        Normalizes the vector, making it to have norm equal to one.
        :return: None
        """
        vec_norm = self.norm()
        if vec_norm == 0.0:
            raise ZeroDivisionError
        self.x /= vec_norm
        self.y /= vec_norm

    def multiply(self, value: float):
        """
        Multiplies the vector by the given value and returns new vector.
        @param value: scalar value to multiply the vector with
        @return: new vector
        """
        x_new = self.x * value
        y_new = self.y * value
        return Vector2d(x_new, y_new)

    def divide(self, value: float) -> "Vector2d":
        """
        Divides the vector by the given value and returns new vector.
        @param value: scalar nonzero value
        @return: new vector
        """
        if value == 0.0:
            raise ZeroDivisionError

        return self.multiply(1.0 / value)

    def copy(self) -> "Vector2d":
        """
        Returns a copy of the vector.
        @return: new vector containing the same coordinates as the current vector
        """
        return Vector2d(self.x, self.y)

    def plus(self, vector: "Vector2d") -> "Vector2d":
        """
        Adds the given vector to the current vector and returns new vector.
        @param vector:
        @return: new vector
        """
        x_new = vector.x + self.x
        y_new = vector.y + self.y
        return Vector2d(x_new, y_new)

    def minus(self, vector: "Vector2d") -> "Vector2d":
        """
        Subtracts the given vector to the current vector and returns new vector.
        @param vector:
        @return: new vector
        """
        return self.plus(vector.multiply(-1))

    def distance(self, vector: "Vector2d") -> float:
        """
        Calculates the distance between two vectors.
        @param vector: other vector to calculate the distance from
        @return: distance
        """
        return self.minus(vector).norm()

    def is_equal(self, vector: "Vector2d") -> bool:
        """
        Checks if two vectors are the same.
        @param vector:
        @return: True if the vector are the same, false otherwise
        """
        return self.x == vector.x and self.y == vector.y


class Circle:
    """
    Represents a circle on the plane.
    """
    def __init__(self, center: Vector2d = None, radius: float = None):

        if center is None:
            center = Vector2d()
        if radius is None:
            radius = float("nan")
        else:
            if radius < 0.0:
                raise ValueError

        self.center: Vector2d = center
        self.radius: float = radius

    def circumference(self) -> float:
        """
        Calculates the circumference of the circle.
        @return:
        """
        return 2.0 * self.radius * math.pi

    def area(self) -> float:
        """
        Calculates the area inside the circle.
        @return:
        """
        return math.pi * self.radius * self.radius

    def distance_from_center(self, point: Vector2d) -> float:
        """
        Calculates the distance between the center and the circle and a point.
        @param point:
        @return: distance from the center of the circle
        """
        return self.center.distance(point)

    def is_inside(self, point: Vector2d) -> bool:
        """
        Checks if the point is inside the circle.
        @param point: a point on the plain
        @return: True if it is inside the circle else False
        """
        return self.distance_from_center(point) < self.radius

    def is_on_boundary(self, point: Vector2d) -> bool:
        """
        Checks if the point is on the boundary of the circle.
        @param point: a point on the plain
        @return: True if it is on the boundary else False
        """
        return self.distance_from_center(point) == self.radius

    def nearest_point_on(self, point: Vector2d) -> Vector2d:
        """
        Finds the nearest point on the circle from the given point.
        @param point: a point on the plain
        @return: closest point on the circle
        """

        # control if input is the center
        if self.center.is_equal(point):
            raise Exception

        direction = point.minus(self.center)
        direction.normalize()

        return direction.multiply(self.radius).plus(self.center)

    def to_string(self) -> str:
        """
        Converts the circle object to its string representation.
        @return: a string representation of the circle object
        """
        radius_string = str(self.radius)
        center_string = self.center.to_string()
        return "[" + radius_string + "; " + center_string + "]"

    def print(self) -> None:
        """
        Prints the circle object to the console window.
        @return: None
        """
        print(self.to_string())
