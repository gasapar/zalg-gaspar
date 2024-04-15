import src.simplefuncs as smfc


if __name__ == '__main__':
    number_list = [-5, -2, -1, 0, 2, 4, 6, 7]
    index = smfc.find_value_in_ordered_list(3, number_list)

    results = smfc.coinChange(569)

    matrix = smfc.create_matrix(3, 4, 2)

    print(matrix[1][2])
    matrix[1][2] = 9

    print(matrix)
    print("***")
    smfc.print_as_matrix(matrix)
    print("***")
