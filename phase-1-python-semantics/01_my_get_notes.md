# 01 - my_get Notes

## Goal

Implement a simplified version of `dict.get`.

Focus:

* key existence
* return value
* no mutation
* aliasing
* assert-based verification

## Correct Implementation

```python
def my_get(d, key, default=None):
    if key in d:
        return d[key]
    else:
        return default
```

## State Model

`my_get` only reads dictionary state.

If key exists:

* check whether key exists in `d`
* read `d[key]`
* return existing value
* no mutation

If key does not exist:

* check whether key exists in `d`
* do not read `d[key]`
* return `default`
* no mutation

## Important Edge Case

```python
assert my_get({"b": 0}, "b", 99) == 0
```

This must return `0`, not `99`.

Reason:

The value `0` is falsy, but the key `"b"` exists.

So the correct check is key existence, not truthiness.

## Mutable Default Aliasing

```python
d = {}
default_list = []
result = my_get(d, "x", default_list)
```

Result:

* `result is default_list` is `True`
* `d` is still `{}`
* aliasing exists between `result` and `default_list`
* `default_list` does not enter `d`

## Mistake I Made

My first wrong version:

```python
def my_get(d, key, default=None):
    if key in d:
        return d[key]
    else:
        d[key] = default
        return d[key]
```

This was wrong because it mutated the dictionary when the key was missing.

That behavior is closer to `setdefault`, not `get`.

## Why the Assert Failed

This passed but polluted state:

```python
assert my_get(d, "x") is None
```

In the wrong version, it secretly did:

```python
d["x"] = None
```

So the next assert failed:

```python
assert my_get(d, "x", 99) == 99
```

Because `"x"` already existed and its value was `None`.

So the real bug was:

Previous assert call mutated shared state.

## Final Takeaway

`get` means:

* read key existence
* if the key exists, return the existing value
* if the key does not exist, return default
* never mutate the dictionary

