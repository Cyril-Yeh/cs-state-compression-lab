def my_counter_add(counter,key):
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1
    return counter[key]

counter = {}
assert my_counter_add(counter, "apple") == 1
assert counter == {"apple": 1}

counter = {"apple": 1}
assert my_counter_add(counter, "apple") == 2
assert counter == {"apple": 2}

counter = {}
my_counter_add(counter, "a")
my_counter_add(counter, "b")
my_counter_add(counter, "a")
assert counter == {
    "a": 2,
    "b": 1,
}

counter = {"x": 10}
result = my_counter_add(counter, "x")
assert result == 11
assert counter["x"] == 11

#counter = {'x': None}
#invariant : counter[key] must be int
