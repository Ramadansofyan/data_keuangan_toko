class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

class HashMap:
    def __init__(self):
        self.map = {}

    def tambah(self, key, value):
        self.map[key] = value

    def cari(self, key):
        return self.map.get(key, None)

    def semua_data(self):
        return self.map
