# 02_my_setdefault

## Model

`setdefault` is not only a read operation.

Its full behavior is:

```text
read state -> branch -> maybe mutate state -> return value
```

## What state does it read?

It reads whether the key exists in the dictionary:

```python
key in d
```

It does **not** check whether the value is truthy.

So this is wrong:

```python
if d.get(key):
    ...
```

Because these are all valid values:

```python
None
0
False
[]
```

A key can exist even if its value is `None`.

## What state does it mutate?

If the key already exists:

```text
do not mutate the dictionary
```

If the key does not exist:

```python
d[key] = default
```

This mutates the original dictionary object passed into the function.

## What does it return?

If the key already exists:

```python
return d[key]
```

It returns the existing value.

If the key does not exist:

```python
d[key] = default
return d[key]
```

It inserts the default value and returns that value.

## Implementation

```python
def my_setdefault(d, key, default=None):
    if key in d:
        return d[key]
    else:
        d[key] = default
        return d[key]
```

## Aliasing

If `default` is a mutable object, `setdefault` does not copy it.

Example:

```python
default_list = []
d = {}

result = my_setdefault(d, "items", default_list)
```

Now these three references point to the same list object:

```python
default_list
result
d["items"]
```

So these are true:

```python
assert result is default_list
assert d["items"] is default_list
```

If I mutate one of them:

```python
result.append(1)
```

Then all three references observe the same changed list.

## Mistake I made

At first, I forgot that `default` should have a default value:

```python
def my_setdefault(d, key, default=None):
```

Without `default=None`, this call would fail:

```python
my_setdefault({}, "x")
```

But it should be valid and should insert:

```python
{"x": None}
```

## Summary

The key lesson is:

```text
key existence is not the same as value truthiness
```

And the operation is:

```text
read key existence
-> if missing, mutate the dictionary
-> return the existing or inserted value
```

