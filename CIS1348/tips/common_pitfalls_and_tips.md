
---
# Common Pitfalls, Tips for Success

---
### Passing a string argument to the `input()` function

When submitting your solutions, ensure your `input()` functions do not contain any strings.
The Reason: In Python, any string passed as an argument to `input()` is automatically written to stdout (standard output).
These prompt strings will be flagged as extra characters, causing your solution to fail.

**Avoid passing string argument to `input()`*
```python
# This will fail
value = input("Please enter a number:")
```

**Instead call `input()` without an argument**
```python
# This will pass
value = input()
```

