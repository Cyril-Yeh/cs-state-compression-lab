def my_defaultdict_get(d, key, factory):
    if key in d:
        return d[key]
    else:
        d[key] = factory()
        return d[key]


d = {"a": 1}
result = my_defaultdict_get(d, "a", list)
assert result == 1
assert d == {"a": 1}

d = {}
result = my_defaultdict_get(d, "items", list)
assert result == []
assert d == {"items": []}
assert result is d["items"]

calls = []
def factory():
    calls.append("called")
    return 99
d = {"x": 10}
result = my_defaultdict_get(d, "x", factory)
assert result == 10
assert calls == []
assert d == {"x": 10}

calls = []
def factory():
    calls.append("called")
    return []
d = {}
result = my_defaultdict_get(d, "x", factory)
result.append(1)
assert calls == ["called"]
assert d == {"x": [1]}
assert result is d["x"]

