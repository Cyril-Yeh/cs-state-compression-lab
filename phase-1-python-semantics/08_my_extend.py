def my_extend(lst, iterable):
    for item in iterable:
        lst[len(lst):] = [item]
    return None

nums = [1]
result = my_extend(nums, [2, 3])
assert nums == [1, 2, 3]
assert result is None

a = []
b = a
my_extend(a, [1, 2])
assert a == [1, 2]
assert b == [1, 2]

items = [[1]]
v = [2]
my_extend(items, [v])
assert items == [[1], [2]]
v.append(3)
assert items == [[1], [2, 3]]

chars = []
my_extend(chars, "abc")
assert chars == ["a", "b", "c"]