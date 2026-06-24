def my_update(target, source):
    for key in source:
            target[key] = source[key]
    return None

target = {"a": 1}
source = {"b": 2}
result = my_update(target, source)
assert result is None
assert target == {"a": 1, "b": 2}
assert source == {"b": 2}

target = {"a": 1, "b": 2}
source = {"b": 99, "c": 3}
result = my_update(target, source)
assert result is None
assert target == {"a": 1, "b": 99, "c": 3}
assert source == {"b": 99, "c": 3}

shared = []
target = {}
source = {"items": shared}
result = my_update(target, source)
assert result is None
assert target["items"] is shared
assert source["items"] is shared
target["items"].append(1)
assert shared == [1]
assert source["items"] == [1]

target = {"a": 1}
source = {}
result = my_update(target, source)
assert result is None
assert target == {"a": 1}
assert source == {}

target = {}
source = {"x": None}
result = my_update(target, source)
assert result is None
assert target == {"x": None}
assert source == {"x": None}