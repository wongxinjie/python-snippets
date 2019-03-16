class ListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class EmptyError(Exception):
    pass


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def insert(self, value):
        if self._tail is None:
            self._tail = ListNode(value, None)
            self._head = self._tail
        else:
            node = ListNode(value, None)
            self._tail.next_node = node
            self._tail = node

    def insert_first(self, value):
        node = ListNode(value, None)
        node.next_node = self._head
        self._head = node

    def search(self, key):
        cursor = self._head
        while cursor and cursor.data != key:
            cursor = cursor.next_node
        return cursor

    def __repr__(self):
        values = []
        cursor = self._head
        while cursor:
            values.append(cursor.data)
            cursor = cursor.next_node

        return ' -> '.join(map(lambda x: str(x), values))

    def remove(self, key):
        if not self._head:
            raise EmptyError("cannot remove item from an empty linked list")

        if self._head.data == key:
            node = self._head
            self._head = self._head.next_node
            return node
        else:
            cursor = self._head
            while cursor and cursor.data != key:
                prev = cursor
                cursor = cursor.next_node

            # found
            if cursor:
                node = cursor
                prev.next_node = cursor.next_node
                if cursor.data == self._tail.data:
                    self._tail = prev
                return node

    def has_cycle(self):
        fast, slow = self._head, self._head
        while fast and fast.next_node and fast.next_node.next_node:
            slow, fast = slow.next_node, fast.next_node.next_node
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    lst = LinkedList()
    for i in range(10):
        lst.insert(i)
    print(lst)
    lst.remove(9)
    print(lst)
    print(lst.has_cycle())
    print(lst._tail.data)
    lst._tail.next_node = lst._head
    print(lst.has_cycle())
