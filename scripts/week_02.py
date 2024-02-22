import src.simplefuncs as smfc
import src.simpleobjects as smobj


if __name__ == '__main__':

    lst = [1, 2, 3, 4, 5, 6, -1, 7, 8, 9, 10]
    min_value, min_idx = smfc.min_of_list(lst)

    vec1 = smobj.Vector2d(x=3, y=4)
    vec2 = vec1.copy()
    vec2.x = 2
