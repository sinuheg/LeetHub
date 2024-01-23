class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity):
        self.map = {}
        self.capacity = capacity
        self.start = None
        self.end = None
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._move_to_top(node)
            return node.value
        else:
            return -1
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_top(node)
        else:
            new_node = Node(key, value)
            self._insert_on_top(new_node)
            self.map[key] = new_node
            if len(self.map) > self.capacity:
                self._remove_last()
    def _move_to_top(self, node):
        if node != self.start:
            self._remove_from_linked_list(node)
            self._insert_on_top(node)
    def _remove_from_linked_list(self, node):
        if node == self.end:
            self.end.next = None
            self.end = self.end.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = None
    def _insert_on_top(self, node):
        if not self.start and not self.end:
            self.start = node
            self.end = node
        else:
            self.start.prev = node
            node.next = self.start
            self.start = node
    def _remove_last(self):
        node = self.end
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.end.next = None
            self.end = self.end.prev
        del self.map[node.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)