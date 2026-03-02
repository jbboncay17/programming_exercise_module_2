d = {"a": [1,2], "b": [3,4]}
d2 = d.copy()
d2["a"].append(5)
print(d["a"])