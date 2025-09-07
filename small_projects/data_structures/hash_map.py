class HashMap:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.hash_map: list[list[tuple[any, any]]] = [[] for _ in range(self.size)]

    def _hash(self, key: any) -> int:
        return hash(key) % self.size

    def insert(self, key: any, value: any) -> None:
        index: int = self._hash(key)
        bucket: list[tuple[any, any]] = self.hash_map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def print_map(self) -> None:
        print(self.hash_map)

    def get(self, key: int) -> any:
        index: int = self._hash(key)
        bucket: list[tuple[any, any]] = self.hash_map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return None

    def delete(self, key: int) -> bool:
        index: int = self._hash(key)
        bucket: list[tuple[any, any]]  = self.hash_map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
