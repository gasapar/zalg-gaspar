import src.containers as containers

if __name__ == '__main__':

    linked_list = containers.LinkedList()

    linked_list.add_first(2)
    linked_list.add_first(1)
    linked_list.add_first(5)
    linked_list.add_first(4)
    linked_list.add_first(3)

    linked_list.print()
    linked_list.bubble_sort()
    linked_list.print()
