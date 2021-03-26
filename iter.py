class DataIteration:
    class IterImpl:
        def __init__(self, data: str):
            self.data = data
            self.n = 0

        def __next__(self):
            if self.n < len(self.data):
                ch = self.data[self.n]
                self.n += 1
                return ch
            else:
                raise StopIteration

    def __init__(self, data: str):
        self.container = data

    def __iter__(self):
        return DataIteration.IterImpl(self.container)
