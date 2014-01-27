class HashTable(object):
    """Simple hash table implementation"""

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def add(self, key, value):
        hashed_key = self._hash(key)
        self.table[hashed_key].append((key, value))

    def get(self, key):
        hashed_key = self._hash(key)
        for entry in self.table[hashed_key]:
            if entry[0] == key:
                return entry[1]
        return None

    def _hash(self, key):
        return hash(key) % self.size

    def __repr__(self):
        return str(self.table)
