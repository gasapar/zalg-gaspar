import src.containers as containers

if __name__ == '__main__':
    bt = containers.BinaryTree()

    bt.add_value(6)
    bt.add_value(1)
    bt.add_value(11)
    bt.add_value(2)
    bt.add_value(8)
    bt.add_value(100)
    bt.add_value(1.5)
    bt.add_value(9)
    bt.add_value(8.5)

    bt.print()
    bt.remove_value(11)
    bt.print()
