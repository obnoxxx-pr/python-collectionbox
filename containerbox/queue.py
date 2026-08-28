from containerbox import Chain


class Queue:
    def __init__(self):
        self._chain = Chain()

    def enqueue(self, item):
        self._chain.append(item)

    def dequeue(self):
        return self._chain.remove_at(0)

    def __len__(self):
        return len(self._chain)

    def __repr__(self):
        return f"Queue({list(self._chain)})"

    def __bool__(self):
        return len(self) > 0
