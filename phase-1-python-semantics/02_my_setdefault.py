def my_setdefault(d, key, default=None):
    if key in d:
        return d[key]
    else:
        d[key] = default
        return d[key]

d = {"a": 1}
result = my_setdefault(d, "a", 99)
assert result == 1
assert d == {"a": 1}

result2 = my_setdefault(d, "b", 99)
assert result2 == 99
assert d == {"a": 1, "b": 99}

d2 = {"x": None}
result3 = my_setdefault(d2, "x", 123)
assert result3 is None
assert d2 == {"x": None}

default_list = []
d3 = {}
result4 = my_setdefault(d3, "items", default_list)
assert result4 is default_list
assert d3["items"] is default_list

d4 = {"items": []}
default_list2 = [1, 2, 3]
result5 = my_setdefault(d4, "items", default_list2)
assert result5 == []
assert result5 is d4["items"]
assert d4["items"] is not default_list2
