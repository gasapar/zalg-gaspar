
class ListElement:
    """
    This class represents a single element in the linked list.
    """
    def __init__(self, value: float = float("nan"), next: "ListElement" = None):
        self.value: float = value
        self.next: "ListElement" = next

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
    def __init__(self, head: ListElement):
        self.current: ListElement = head

    def __iter__(self):
        return self

    def __next__(self) -> ListElement:
        if not self.current:
            raise StopIteration
        else:
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

        new_element = ListElement(value=value, next=self.head)
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

        new_element = ListElement(value=value, next=item.next)
        item.next = new_element

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

    def add_sorted(self, value: float) -> None:
        """
        Adds a value to the sorted list so that the list remains sorted.
        @param value: new value to be added
        @return: None
        """
        if self.is_empty():
            self.add_to_empty(value)
            return

        if not self.is_sorted():
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
