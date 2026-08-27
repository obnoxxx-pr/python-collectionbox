from containerbox import Chain

class Stack:
    def __init__(self):
        self._chain = Chain()

    def push(self, item):
        self._chain.prepend(item)

    def pop(self):
        return self._chain.remove_at(0)
    def __len__(self):
        return len(self._chain)
    def __bool(self):
        return len(self) > 0
    def peek(self):
        return self._chain.get_head()

