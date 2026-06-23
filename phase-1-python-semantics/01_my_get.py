def my_get(d, key, default=None):
    if key in d:
        return d[key]
    else:
        return default


d = {"a": 1, "b": 0, "c": None, "d": []}

assert my_get(d, "a") == 1
assert my_get(d, "b") == 0
assert my_get(d, "c") is None
assert my_get(d, "x") is None

assert my_get(d, "x", 99) == 99
assert my_get(d, "b", 99) == 0
assert my_get(d, "c", 99) is None

default_list = []
result = my_get(d, "x", default_list)
assert result is default_list

existing_list = d["d"]
result2 = my_get(d, "d", [])
assert result2 is existing_list

assert d == {"a": 1, "b": 0, "c": None, "d": []}