class ListElement:
    """
    This class represents a single element in the linked list.
    """

    def __init__(self, value: float = float("nan"), next_element: "ListElement" = None):
        self.value: float = value
        self.next: "ListElement" = next_element

    def is_last(self) -> bool:
        """
        Checks if the element is last or not.
        @return: returns true if the element is last, false otherwise
        """
        return self.next is None

    def to_string(self) -> str:
        """
        Converts the element to the string.
        @return: text representation of the element
        """
        return str(self.value)


class LinkedListIterator:
    """
    This class implements iterator for class LinkedList.
    """

    def __init__(self, head: ListElement | None):
        self.current: ListElement | None = head

    def __iter__(self):
        return self

    def __next__(self) -> ListElement:
        if not self.current:
            raise StopIteration

        current_item: ListElement = self.current
        self.current = self.current.next
        return current_item


class LinkedList:
    """
    This class represents a linked list.
    """

    def __init__(self):
        self.head: ListElement | None = None
        self.tail: ListElement | None = None

    def __iter__(self) -> LinkedListIterator:
        """
        Iterates through the linked list.
        @return: returns iterator
        """
        return LinkedListIterator(self.head)

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        @return: true if the list is empty, false otherwise
        """
        return self.head is None and self.tail is None

    def add_to_empty(self, value: float) -> None:
        """
        Adds a value to the empty list.
        @param value: new value to be added to the list
        @return: None
        """
        new_element = ListElement(value=value)
        self.head = new_element
        self.tail = new_element

    def add_first(self, value: float) -> None:
        """
        Adds a value to the beginning of the list.
        @param value: new value to be added to the list
        @return: None
        """
        if self.is_empty():
            self.add_to_empty(value)
            return

        new_element = ListElement(value=value, next_element=self.head)
        self.head = new_element

    def add_last(self, value: float) -> None:
        """
        Adds a value to the end of the list.
        @param value: new value to be added to the list
        @return: None
        """
        if self.is_empty():
            self.add_to_empty(value)

        new_element = ListElement(value=value)
        self.tail.next = new_element
        self.tail = new_element

    def to_string(self) -> str:
        """
        Returns a string representation of the linked list.
        @return: text representation of the linked list
        """
        full_string: str = "["
        # iterator is used, no need to use while cycles
        for current_item in self:
            full_string += current_item.to_string()
            if not current_item.is_last():
                full_string += ", "

        full_string += "]"
        return full_string

    def print(self) -> None:
        """
        Prints the linked list.
        @return: None
        """
        print(self.to_string())

    def remove_first(self) -> None:
        """
        Removes the first element from the linked list.
        @return: None
        """
        if self.is_empty():
            return

        # case when only a single item is in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        return

    def sum(self) -> float:
        """
        Returns the sum of the values in the linked list.
        @return: total sum of the values in the linked list
        """
        if self.is_empty():
            return float("nan")

        total_sum: float = 0.0
        for item in self:
            total_sum += item.value
        return total_sum

    def prod(self) -> float:
        """
        Returns the product of the values in the linked list.
        @return: product of the values in the linked list
        """
        if self.is_empty():
            return float("nan")

        total_sum: float = 1.0
        for item in self:
            total_sum *= item.value
        return total_sum

    def min(self) -> float:
        """
        Returns the minimal value of the elements in the list.
        @return: minimum value of the elements in the list
        """
        if self.is_empty():
            return float("nan")

        current_min: float = float("inf")
        for item in self:
            if item.value < current_min:
                current_min = item.value
        return current_min

    def max(self) -> float:
        """
        Returns the maximal value of the elements in the list.
        @return: maximum value of the elements in the list
        """
        if self.is_empty():
            return float("nan")

        current_max: float = -float("inf")
        for item in self:
            if item.value > current_max:
                current_max = item.value
        return current_max

    def mean(self) -> float:
        """
        Returns arithmetic mean of the elements in the list.
        @return: mean value of the elements in the list
        """
        if self.is_empty():
            return float("nan")

        item_counter: int = 0
        total_sum: float = 0.0
        for item in self:
            total_sum += item.value
            item_counter += 1

        return total_sum / item_counter

    def add_after(self, value: float, item: ListElement) -> None:
        """
        Adds a value to the list after the given element.
        @param value: new value to be added
        @param item: element after which to add the value
        @return: None
        """
        if item == self.tail:
            self.add_last(value)
            return

        if self.is_empty():
            raise Exception

        new_element = ListElement(value=value, next_element=item.next)
        item.next = new_element

    def remove_after(self, item: ListElement) -> None:
        """
        Removes a value from the list after the given element.
        @param item:
        @return:
        """
        return

    def find_value(self, value: float) -> ListElement | None:
        """
        Finds the item containing the given value.
        @param value: The number to be found
        @return: Element containing the value or None
        """""
        return None

    def is_sorted(self) -> bool:
        """
        Returns whether the list is sorted or not.
        @return: True if the list is sorted, False otherwise
        """

        if self.is_empty():
            # empty list is always sorter
            return True

        if self.head == self.tail:
            # list with a single value is always sorter
            return True

        for item in self:
            # must check that item.next is not None and then compares the pair
            if item.next and item.value > item.next.value:
                return False
        return True

    def add_sorted(self, value: float, enforce_sorted: bool = False) -> None:
        """
        Adds a value to the sorted list so that the list remains sorted.
        @param value: new value to be added
        @param enforce_sorted: whether to allow for adding a value into an unsorted list
        @return: None
        """
        if self.is_empty():
            self.add_to_empty(value)
            return

        if enforce_sorted and not self.is_sorted():
            # cannot add a new value to the unsorted list
            raise Exception

        if value >= self.tail.value:
            self.add_last(value)
            return

        if value <= self.head.value:
            self.add_first(value)
            return

        for item in self:
            if item.next and item.value <= value <= item.next.value:
                self.add_after(value, item)
                return

    def single_bubble(self) -> int:
        """
        Returns the number of switched value pairs in single bubble sort run.
        @return: number of switched pairs
        """
        bubble_counter: int = 0
        for item in self:
            if item.next and item.value > item.next.value:
                bubble_counter += 1
                # switch values
                item.value, item.next.value = item.next.value, item.value
        return bubble_counter

    def bubble_sort(self) -> None:
        """
        Sorts the list using bubble sort approach.
        @return: None
        """
        if self.is_empty():
            return

        if self.head == self.tail:
            return

        counter: int = 1
        while counter != 0:
            counter = self.single_bubble()


class BinaryNode:
    """
    Class representing a node in a binary tree.
    """
    def __init__(self, value: float = float("nan"), left=None, right=None, parent=None, tree=None):
        self.left = left
        self.right = right
        self.value: float = value

        self.parent = parent
        self.tree: BinaryTree | None = tree

    def is_leaf(self) -> bool:
        """
        Returns true if the node is a leaf node.
        @return: True if the node is a leaf, False otherwise
        """
        return self.left is None and self.right is None

    def is_root(self) -> bool:
        """
        Returns true if the node is a root in the tree.
        @return: True if the node is a root, False otherwise
        """
        if self.tree is None:
            return False
        return self.tree.root is self

    def add_value(self, value: float) -> None:
        """
        Adds a value to the subtree starting with this node.
        @param value: number to add to the subtree
        @return: None
        """
        if self.value == value:
            # this value is already in the node/tree, do not add again
            return

        if value < self.value:
            # adding to the left
            if self.left is None:
                # left is empty, create new node
                self.left = BinaryNode(value=value, parent=self, tree=self.tree)
            else:
                # add to the subtree
                self.left.add_value(value=value)
        else:
            # adding to the right
            if self.right is None:
                # right is empty, create new node
                self.right = BinaryNode(value=value, parent=self, tree=self.tree)
            else:
                # add to the subtree
                self.right.add_value(value=value)

    def to_list(self) -> list[float]:
        """
        Converts the subtree to a list of numbers.
        @return: List of sorted numbers from the tree
        """
        left_list = []
        if self.left is not None:
            left_list = self.left.to_list()

        center_list = [self.value]

        right_list = []
        if self.right is not None:
            right_list = self.right.to_list()

        return left_list + center_list + right_list

    def find_value(self, value: float):
        """
        Returns the node containing given value or None.
        @param value:
        @return: Binary node containing given value or None
        """
        if self.value == value:
            return self

        if value < self.value:
            # search left
            if self.left is None:
                return None
            else:
                return self.left.find_value(value)
        else:
            # search right
            if self.right is None:
                return None
            else:
                return self.right.find_value(value)

    def replace_child(self, child: "BinaryNode", new_child=None) -> None:
        """
        Replaces any children of this node with given new child.
        @param child:
        @param new_child:
        @return:
        """
        if self.left is child:
            self.left = new_child

        if self.right is child:
            self.right = new_child

    def replace_at_parent(self, new_child=None) -> None:
        """
        Replaces itself at parent with new child.
        @param new_child:
        @return:
        """
        # special case: self is root
        if self.is_root():
            self.tree.root = new_child

        if self.parent is None:
            return
        self.parent.replace_child(self, new_child)

    def num_children(self) -> int:
        """
        Returns the number of valid children.
        @return: Number of valid children: 0-2
        """
        counter = 0
        if self.left:  # if self.left is not None
            counter += 1
        if self.right:
            counter += 1
        return counter

    def get_single_child(self) -> "BinaryNode":
        """
        Get valid (not None) child.
        @return:
        """
        if self.left:
            return self.left
        return self.right

    def get_most_right(self) -> "BinaryNode":
        """
        Get most right (maximal) node in the subtree.
        @return:
        """
        if self.right:
            return self.right.get_most_right()
        # no right child exists, self is the most right
        return self


class BinaryTree:
    """
    Binary tree containing numbers.
    """
    def __init__(self):
        self.root: BinaryNode | None = None

    def is_empty(self) -> bool:
        """
        Returns True if tree is empty, False otherwise.
        @return:
        """
        return self.root is None

    def add_value(self, value: float) -> None:
        """
        Adds given value into the tree.
        @param value:
        @return:
        """
        if self.is_empty():
            self.root = BinaryNode(value=value, tree=self)
            return

        self.root.add_value(value=value)

    def to_list(self) -> list[float]:
        """
        Converts the tree to a list of floats.
        @return:
        """
        if self.is_empty():
            return []

        return self.root.to_list()

    def print(self) -> None:
        """
        Prints the tree as a list of values.
        @return:
        """
        print(self.to_list())

    def find_value(self, value: float) -> BinaryNode | None:
        """
        Finds the value in the tree and returns the node if it exists.
        @param value:
        @return:
        """
        if self.is_empty():
            return None

        return self.root.find_value(value=value)

    def remove_value(self, value: float) -> None:
        """
        Removes the value from the tree.
        @param value:
        @return: None
        """
        if self.is_empty():
            return None

        node = self.find_value(value=value)
        if node is None:
            # value is not in the tree
            return

        self.remove_node(node=node)

    def remove_node(self, node: BinaryNode | None = None) -> None:
        """
        Removes the value from the given node from the tree.
        @param node: node containing the value to be removed
        @return: None
        """
        if node is None:
            return

        if node.is_leaf():
            node.replace_at_parent(new_child=None)
            return

        if node.num_children() == 1:
            child = node.get_single_child()
            child.parent = node.parent
            node.replace_at_parent(new_child=child)
            return

        # case: node has both children
        to_replace = node.left.get_most_right()
        node.value = to_replace.value
        self.remove_node(node=to_replace)
