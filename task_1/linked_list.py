class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def print_list(self):
        current = self.head
        print("head")
        while current:
            print(current.data)
            current = current.next
        print("tail")

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    @staticmethod
    def merge(left, right):
        merged_list = LinkedList()
        current_left_node = left.head
        current_right_node = right.head
        while current_left_node is not None and current_right_node is not None:
            if current_left_node.data <= current_right_node.data:
                merged_list.append(current_left_node.data)
                current_left_node = current_left_node.next
            else:
                merged_list.append(current_right_node.data)
                current_right_node = current_right_node.next

        if current_left_node is not None:
            merged_list.append(current_left_node.data)

        elif current_right_node is not None:
            merged_list.append(current_right_node.data)

        merged_list.reverse()
        return merged_list

    def sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.__sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def __sorted_insert(self, head_ref, new_node):
        if not head_ref or head_ref.data >= new_node.data:
            new_node.next = head_ref
            head_ref = new_node
        else:
            node = self.__find_node(head_ref, new_node.data)
            self.__insert(node, new_node)
        return head_ref

    def __find_node(self, start_node, data):
        current = start_node
        while current.next and current.next.data < data:
            current = current.next
        return current

    def __insert(self, node, new_node):
        new_node.next = node.next
        node.next = new_node


def main():
    print("-- First Unsorted --")
    l1 = LinkedList()
    l1.append(3)
    l1.append(1)
    l1.append(2)
    l1.append(5)
    l1.print_list()

    print("-- First Sorted --")
    l1.sort()
    l1.print_list()

    print("-- Second Unsorted--")
    l2 = LinkedList()
    l2.append(2)
    l2.append(1)
    l2.append(3)
    l2.append(4)
    l2.print_list()

    print("-- Second Sorted--")
    l2.sort()
    l2.print_list()

    print("-- Merge First and Second--")
    l3 = LinkedList.merge(l1, l2)
    l3.print_list()

    print("---------------")
    l1.print_list()
    l2.print_list()


if __name__ == "__main__":
    main()
