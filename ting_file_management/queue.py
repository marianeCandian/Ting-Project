from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)
        else:
            return None

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def search(self, value):
        if value < 0 or value >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[value]
