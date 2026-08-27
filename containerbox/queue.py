from containerbox import Chain

class Queue:
    def __init__(self):
        self._chain = Chain()

    def enqueue(self, item):
        self._chain.append(item)

    def dequeue(self):
        return self._chain.remove_at(0)
