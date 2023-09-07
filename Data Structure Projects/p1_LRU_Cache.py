from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.our_cache = OrderedDict()

    def get(self, key):
        if key not in self.our_cache:
            return -1
        else:
            self.our_cache.move_to_end(key)
            return self.our_cache[key]

    def set(self, key, value):
        self.our_cache[key] = value
        self.our_cache.move_to_end(key)
        if len(self.our_cache) > self.capacity:
            self.our_cache.popitem(last=False)


our_cache = LRU_Cache()

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.our_cache)  # prints key/value pairs currently in dictionary

our_cache.get(1)
our_cache.get(2)
print(our_cache.get(9))  # prints -1 because value not in cache
print(our_cache.our_cache)

our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # prints -1 because value not in cache
print(our_cache.our_cache)

# Test Case 1
our_cache.set(7, 7)
print(our_cache.get(7))  # prints 7
print(our_cache.our_cache)
# Test Case 2
our_cache.set(8, "test")
print(our_cache.get(8))  # prints "test"
print(our_cache.our_cache)
# Test Case 3
our_cache.set(9, 8675309)
print(our_cache.get(9))  # prints 8675309
print(our_cache.our_cache)

our_cache2 = LRU_Cache()

our_cache2.set(1, 9 * 9)
our_cache2.set(2, 2 * "times")
print(our_cache2.our_cache)  # prints key/value pairs currently in dictionary

our_cache2.get(1)
our_cache2.get(2)
print(our_cache2.get(9 * 9))  # noqa prints -1 since value not in cache due to get format
print(our_cache2.our_cache)

our_cache2.set(5, 5)
our_cache2.set(6, 6)
print(our_cache2.get("hi"))  # prints -1 because value not in cache
print(our_cache2.our_cache)

# Test Case 1
our_cache2.set(7, "hi")
print(our_cache2.get(7))  # prints hi
print(our_cache2.our_cache)
# Test Case 2
our_cache2.set(8, " ")
print(our_cache2.get(8))  # prints a space
print(our_cache2.our_cache)
# Test Case 3
our_cache2.set(9, 8675309)
print(our_cache2.get(99))  # prints nothing due to get typo
print(our_cache2.our_cache)

our_cache3 = LRU_Cache()

our_cache3.set(1, 1)
our_cache3.set(2, 1.1)
print(our_cache3.our_cache)  # prints key/value pairs currently in dictionary

our_cache3.get(1)
our_cache3.get(2)
print(our_cache3.get(.1 * .1))  # noqa prints -1 since value not in cache due to get format
print(our_cache3.our_cache)

our_cache3.set(5, 5)
our_cache3.set(6, 6)
print(our_cache3.get("hi"))  # prints -1 because value not in cache
print(our_cache3.our_cache)

# Test Case 1
our_cache3.set(7, .1 * .1)
print(our_cache3.get(7))  # prints 0.010000000000000002
print(our_cache3.our_cache)
# Test Case 2
our_cache3.set(8, .1 + .1)
print(our_cache3.get(8))  # prints 0.2
print(our_cache3.our_cache)
# Test Case 3
our_cache3.set(9, .1 / .1)
print(our_cache3.get(9))  # prints 1
print(our_cache3.our_cache)
