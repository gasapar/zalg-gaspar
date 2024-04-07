import src.containers as containers
import psutil
import random


if __name__ == '__main__':
    process = psutil.Process()

    num_elements = 10_000
    num_repeats = 10

    print(process.memory_info().rss)

    for _ in range(num_repeats):
        container = containers.BinaryTree()
        for _ in range(num_elements):
            container.add_value(random.random())

        print(process.memory_info().rss)

    print("***")

