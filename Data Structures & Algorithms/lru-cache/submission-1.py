class Node:
    def __init__(self, val = None, key = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Linked list for usage booking
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        # Hash map for fast retrieval
        self.d = dict()

    def get(self, key: int) -> int:
        node = self.d.get(key)

        if node is None:
            return -1

        self._remove(node)
        self._add_to_tail(node)

        return node.val

    def put(self, key: int, val: int) -> None:
        node = self.d.get(key)

        if node is not None:
            self._remove(node)
            self._add_to_tail(node)
            node.val = val
        else:
            if len(self.d) == self.capacity:
                to_pop = self.head.next
                self.d.pop(to_pop.key)
                self.head.next = to_pop.next
                to_pop.next.prev = self.head
                del(to_pop)

            node = Node(val, key)
            self.d[key] = node
            self._add_to_tail(node)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

            

        
