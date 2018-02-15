# https://leetcode.com/problems/lru-cache/description/
class Node():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class dll(object):
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.count = 0

    def push(self, node):
        if self.count == 0:
            self.head = self.tail = node
        else: 
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
        self.count += 1

    def pop(self):
        if self.tail is None:
            return None
        elif self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            oldTail = self.tail
            newTail = self.tail.prev
            newTail.next = None
            oldTail.prev = None
            self.tail = newTail
            self.count -= 1
            return oldTail
    
    def remove(self, node):
        if self.tail is None:
            return None
        elif self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        elif self.head == node:
            oldHead = self.head
            newHead = self.head.next
            newHead.prev = None
            oldHead.next = None
            self.head = newHead
            self.count -= 1
        elif self.tail == node:
            oldTail = self.tail
            newTail = self.tail.prev
            newTail.next = None
            oldTail.prev = None
            self.tail = newTail
            self.count -= 1
        else:
            node.prev.next = node.next
            node.next.prev= node.prev
            self.count -= 1

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.dll = dll()

    def get(self, key):
        if self.capacity == 0:
            return -1
        elif key not in self.storage:
            return -1
        else:
            location = self.storage[key]['location']
            self.dll.remove(location)
            self.dll.push(location)
            return self.storage[key]['value']

    def put(self, key, value):
        if self.capacity == 0:
            return None
        elif len(self.storage) < self.capacity and key not in self.storage:
            self.storage[key] = {'value': value}
            node = Node(key)
            self.dll.push(node)
            self.storage[key]['location'] = self.dll.head
        elif key in self.storage:
            self.get(key)
            self.storage[key]['value'] = value
        else:
            deleteNode = self.dll.tail.val
            self.dll.pop()
            del self.storage[deleteNode]
            self.storage[key] = {'value': value}
            node = Node(key)
            self.dll.push(node)
            self.storage[key]['location'] = self.dll.head

        
cache = LRUCache( 10 )

cache.put(10, 13)
cache.put(3, 17)
cache.put(6, 11)
cache.put(10, 5)
cache.put(9, 10)
print(cache.get(13), -1)
cache.put(2, 19)
print(cache.get(2), 19)
print(cache.get(3), 17)
cache.put(5, 25)
print(cache.get(8), -1)
cache.put(9, 22)
cache.put(5, 5)
cache.put(1, 30)
print(cache.get(11), -1)
cache.put(9, 12)
print(cache.get(7), -1)
print(cache.get(5), 5)
print(cache.get(8), -1)
print(cache.get(9), 12)
cache.put(4, 30)
cache.put(9, 3)
print(cache.get(9), 3)
print(cache.get(10), 5)
print(cache.get(10), 5)
cache.put(6, 14)
cache.put(3, 1)
print(cache.get(3), 1)
cache.put(10, 11)
print(cache.get(8), -1)
cache.put(2, 14)
print(cache.get(1), 30)
print(cache.get(5), 5)
print(cache.get(4), 30)
cache.put(11, 4)
cache.put(12, 24)
cache.put(5, 18)
print(cache.get(13), -1)
cache.put(7, 23)
print(cache.get(8), -1)
print(cache.get(12), 24)
cache.put(3, 27)
cache.put(2, 12)
print(cache.get(5), 18)
cache.put(2, 9)
cache.put(13, 4)
cache.put(8, 18)
cache.put(1, 7)
print(cache.get(6), 14)
cache.put(9, 29)
cache.put(8, 21)
print(cache.get(5), 18)
cache.put(6, 30)
cache.put(1, 12)
print(cache.get(10), 11)
cache.put(4, 15)
cache.put(7, 22)
cache.put(11, 26)
cache.put(8, 17)
cache.put(9, 29)
print(cache.get(5), 18)
cache.put(3, 4)
cache.put(11, 30)
print(cache.get(12), -1)
cache.put(4, 29)
print(cache.get(3), 4)
print(cache.get(9), 29)
print(cache.get(6), 30)
cache.put(3, 4)
print(cache.get(1), 12)
print(cache.get(10), 11)
cache.put(3, 29)
cache.put(10, 28)
cache.put(1, 20)
cache.put(11, 13)
print(cache.get(3), 29)
cache.put(3, 12)
cache.put(3, 8)
cache.put(10, 9)
cache.put(3, 26)
print(cache.get(8), 17)
print(cache.get(7), -1)
print(cache.get(5), 18)
cache.put(13, 17)
cache.put(2, 27)
cache.put(11, 15)
print(cache.get(12), -1)
cache.put(9, 19)
cache.put(2, 15)
cache.put(3, 16)
print(cache.get(1), 20)
cache.put(12, 17)
cache.put(9, 1)
cache.put(6, 19)
print(cache.get(4), 29)
print(cache.get(5), 18)
print(cache.get(5), 18)
cache.put(8, 1)
cache.put(11, 7)
cache.put(5, 2)
cache.put(9, 28)
print(cache.get(1), 20)
cache.put(2, 2)
cache.put(7, 4)
cache.put(4, 22)
cache.put(7, 24)
cache.put(9, 26)
cache.put(13, 28)
cache.put(11, 26)
