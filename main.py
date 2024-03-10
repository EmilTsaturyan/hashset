from typing import Any

import hashlib

class HashSet:
    """
    Mutable sequence.

    If no argument is given, the constructor creates a new empty hash set. The argument must be an iterable if specified.
    """
    def __init__(self) -> None:
        # Initialize the buckets and the list to store elements
        self.buckets: list[list[Any]] = [[], [], [], [], []]
        self.lst: list[Any] = []

    def __str__(self) -> str:
        # Convert the list representation to a string for easy printing
        return f'{self.lst}'

    def __contains__(self, obj: Any) -> bool:
        # Check if the object is present in the hash set
        bucket = self.__custom_hash(obj)
        return obj in self.buckets[bucket]

    def __getitem__(self, index: int) -> Any:
        # Get an item from the list using index
        return self.lst[index]

    def add(self, obj: Any) -> None:
        # Add an object to the hash set
        if obj not in self:
            # Resize if the number of elements exceeds the number of buckets
            if len(self.lst) == len(self.buckets):
                self.__resize()

            # Calculate the hash and add the object to the appropriate bucket
            bucket = self.__custom_hash(obj)
            self.buckets[bucket].append(obj)
            self.lst.append(obj)

    def remove(self, obj: Any) -> None:
        # Remove an object from the hash set
        bucket = self.__custom_hash(obj)
        if obj in self.buckets[bucket]:
            self.buckets[bucket].remove(obj)
            self.lst.remove(obj)

    def __custom_hash(self, obj: Any) -> int:
        # Custom hash function using SHA-256
        obj_bytes = str(obj).encode('utf-8')
        sha256_hash = hashlib.sha256(obj_bytes)
        hash_integer = int(sha256_hash.hexdigest(), 16)
        return hash_integer % len(self.buckets)

    def __resize(self) -> None:
        # Double the number of buckets and rehash the elements
        self.buckets = [[] for _ in range(len(self.buckets) * 2)]
        for item in self.lst:
            bucket = self.__custom_hash(item)
            self.buckets[bucket].append(item)

# Example usage
hashset = HashSet()
hashset.add(45)
hashset.add(69)
