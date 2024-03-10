# HashSet Implementation

## Description

This is a Python implementation of a HashSet, a mutable sequence. The HashSet uses a custom hash function based on SHA-256 for efficient element storage and retrieval. It supports adding, removing, and checking the existence of elements.

## Class: `HashSet`

### Methods

1. `__init__(self) -> None`

   - Constructor that initializes the HashSet with empty buckets and an empty list.

2. `__str__(self) -> str`

   - Converts the HashSet to a string for easy printing.

3. `__contains__(self, obj: Any) -> bool`

   - Checks if an object is present in the HashSet.

4. `__getitem__(self, index: int) -> Any`

   - Retrieves an item from the HashSet using the provided index.

5. `add(self, obj: Any) -> None`

   - Adds an object to the HashSet.

6. `remove(self, obj: Any) -> None`

   - Removes an object from the HashSet.

7. `__custom_hash(self, obj: Any) -> int`

   - Custom hash function using SHA-256.

8. `__resize(self) -> None`

   - Doubles the number of buckets and rehashes the elements when the number of elements exceeds the number of buckets.

## Example Usage

```python
hashset = HashSet()
hashset.add(45)
hashset.add(69)
