import src.simpleobjects as smobj


if __name__ == '__main__':
    vec1 = smobj.Vector2d(0, 0)
    vec2 = smobj.Vector2d(0, 2)
    radius = 1.0

    circ = smobj.Circle(vec1, radius)

    vec3 = circ.nearest_point_on(vec2)
