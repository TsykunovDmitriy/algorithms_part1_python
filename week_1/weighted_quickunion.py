class WeighedQuickUnion:
    def __init__(self, N):
        self.id = list(range(N))
        self.sizes = [1 for _ in self.id]

    def _root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        if not self.connected(p, q):
            i = self._root(p)
            j = self._root(q)

            if self.sizes[i] >= self.sizes[j]:
                self.id[j] = i
                self.sizes[i] += self.sizes[j]
            else:
                self.id[i] = j
                self.sizes[j] += self.sizes[i]

        