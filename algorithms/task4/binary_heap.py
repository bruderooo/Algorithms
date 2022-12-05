class BinaryHeap:
    def __init__(self):
        self._heap = []

    def pop(self):
        last_item = self._heap.pop()
        if self:
            smallest_one = self._heap[0]
            self._heap[0] = last_item
            self._siftup(0)
            return smallest_one
        return last_item

    def push(self, item: tuple[int | float, str]):
        self._heap.append(item)
        self._siftdown(0, len(self._heap) - 1)

    def __str__(self):
        return str(self._heap)

    def __bool__(self):
        return bool(self._heap)

    def _siftdown(self, startpos: int, pos: int):
        newitem = self._heap[pos]

        while pos > startpos:
            parent_pos = (pos - 1) // 2
            if newitem[0] < (parent := self._heap[parent_pos])[0]:
                self._heap[pos] = parent
                pos = parent_pos
                continue
            break
        self._heap[pos] = newitem

    def _siftup(self, pos: int):
        endpos = len(self._heap)
        startpos = pos
        newitem = self._heap[pos]

        childpos = 2 * pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and self._heap[childpos][0] >= self._heap[rightpos][0]:
                childpos = rightpos

            self._heap[pos] = self._heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1

        self._heap[pos] = newitem
        self._siftdown(startpos, pos)
