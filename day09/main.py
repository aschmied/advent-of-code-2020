import collections

class LastN:
    def __init__(self, number_to_keep):
        self._number_to_keep = number_to_keep
        self._queue = collections.deque()
        self._counts = collections.defaultdict(lambda: 0)

    def add(self, obj):
        self._append_to_queue(obj)
        self._add_to_counts(obj)
        if len(self._queue) > self._number_to_keep:
            removed = self._pop_from_queue(obj)
            self._remove_from_counts(removed)

    def _append_to_queue(self, obj):
        self._queue.append(obj)

    def _add_to_counts(self, obj):
        self._counts[obj] += 1

    def _pop_from_queue(self, obj):
        return self._queue.popleft()

    def _remove_from_counts(self, obj):
        self._counts[obj] -= 1
        if self._counts[obj] == 0:
            del(self._counts[obj])

    def count(self, obj):
        return self._counts[obj]

    def __len__(self):
        return len(self._queue)

    def __contains__(self, obj):
        return obj in self._counts.keys()
