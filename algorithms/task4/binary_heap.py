from algorithms.task4.prioritized_item import PrioritizedItem


class BinaryHeap:
    def __init__(self):
        self._heap = []

    def push(self, value: tuple[int, str]):
        self.push_item(PrioritizedItem(*value))

    def push_item(self, value: PrioritizedItem):
        self._heap.append(value)
        self.sift_down(len(self._heap) - 1)

    def pop(self):
        last_item = self._heap.pop()
        if self:
            smallest_one = self._heap[0]
            self._heap[0] = last_item
            self.sift_up()
            return smallest_one
        return last_item

    def __str__(self):
        return str(self._heap)

    def __bool__(self):
        return bool(self._heap)

    def sift_down(self, pos: int):
        new_item = self._heap[pos]

        while pos > 0:
            parent_pos = (pos - 1) // 2
            if new_item >= (parent := self._heap[parent_pos]):
                break
            else:
                self._heap[pos] = parent
                pos = parent_pos

        self._heap[pos] = new_item

    def sift_up(self):
        pos = 0
        size = len(self._heap)
        new_item = self._heap[pos]

        left_child_index = 2 * pos + 1
        while left_child_index < size:
            right_child_index = left_child_index + 1
            if right_child_index < size and self._heap[left_child_index] >= self._heap[right_child_index]:
                left_child_index = right_child_index

            self._heap[pos] = self._heap[left_child_index]
            pos = left_child_index
            left_child_index = 2 * pos + 1

        self._heap[pos] = new_item
        self.sift_down(pos)
