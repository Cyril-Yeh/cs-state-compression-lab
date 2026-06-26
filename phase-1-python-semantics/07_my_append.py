def my_append(lst, value):
    lst[len(lst):] = [value]
    return None


nums = [1, 2]
result = my_append(nums, 3)
assert nums == [1, 2, 3]
assert result is None

shared = []
a = shared
b = shared
my_append(a, 10)
assert a == [10]
assert b == [10]

items = [[1]]
my_append(items, [2])
assert items == [[1], [2]]

x = [1]
y = x
my_append(x, 2)
assert y == [1, 2]
