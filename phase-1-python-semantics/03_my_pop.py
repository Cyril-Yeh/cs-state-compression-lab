def my_pop(d,key,default=None):
    if key in d:
        removal_value = d[key]
        del d[key]
        return removal_value
    else:
        return default

d = {"a": 1, "b": 2}
result = my_pop(d, "a")
assert result == 1
assert d == {"b": 2}

d = {"a": 1}
result = my_pop(d, "x", 99)
assert result == 99
assert d == {"a": 1}

d = {"a": None}
result = my_pop(d, "a", 99)
assert result is None
assert d == {}

value = []
d = {"items": value}
result = my_pop(d, "items")
assert result is value
assert d == {}
result.append(1)
assert value == [1]

default = []
d = {"a": 1}
result = my_pop(d, "missing", default)
assert result is default
assert d == {"a": 1}
result.append("x")
assert default == ["x"]