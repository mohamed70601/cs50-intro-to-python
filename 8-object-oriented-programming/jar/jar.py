class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be a non-negative integer")
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError("Above capacity")

    def withdraw(self, n):
        if n <= self._size:
            self._size -= n
        else:
            raise ValueError("Can't exceed number of stored")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
