class Node:
    """One entry in the doubly linked list."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}                      # key -> Node (for O(1) lookup)

        # Dummy head and tail so we never have to handle "empty list" edge cases.
        # head.next = most recently used, tail.prev = least recently used.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # small helpers (each is O(1)) 
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    #  public operations 
    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)             # move it to the front = "recently used"
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:            # update existing key
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        if len(self.map) >= self.capacity:   # full -> evict least recently used
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    print(cache.get(1))    # 10  (key 1 is now most recent)
    cache.put(3, 30)       # evicts key 2
    print(cache.get(2))    # -1
    cache.put(4, 40)       # evicts key 1
    print(cache.get(1))    # -1
    print(cache.get(3))    # 30
    print(cache.get(4))    # 40
