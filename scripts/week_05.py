import src.containers as containers

if __name__ == '__main__':

    linked_list = containers.LinkedList()

    linked_list.add_first(9)
    linked_list.add_first(5)
    linked_list.add_first(10)
    linked_list.add_first(-8)

    linked_list.print()

    sum_value = linked_list.sum()
    product_value = linked_list.prod()
    min_value = linked_list.min()
    max_value = linked_list.max()
    mean_value = linked_list.mean()
