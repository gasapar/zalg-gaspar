
class ListElement:
    """
    This class represents a single element in the linked list.
    """
    def __init__(self, value: float = float("nan"), next: "ListElement" = None):
        self.value: float = value
        self.next: "ListElement" = next

    def is_last(self) -> bool:
        """
        Checks if the element point to None and if therefore the last in the list.
        :return: True if the element point to None
        """
        return self.next is None


class LinkedList:
    """
    This class represents a linked list.
    """
    def __init__(self):
        self.head: ListElement = None
        self.tail: ListElement = None

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        :return: True if the list is empty
        """
        return self.head is None and self.tail is None

    def add_to_empty(self, value: float) -> None:
        """
        Adds a value to the empty list.
        """
        new_element = ListElement(value=value)
        self.head = new_element
        self.tail = new_element

    def add_first(self, value: float) -> None:
        """
        Adds a value to the beginning of the list.
        """

        if self.is_empty():
            self.add_to_empty(value)
            return

        new_element = ListElement(value=value, next=self.head)
        self.head = new_element

    def add_last(self, value: float) -> None:
        if self.is_empty():
            self.add_to_empty(value)

        new_element = ListElement(value=value)
        self.tail.next = new_element
        self.tail = new_element






