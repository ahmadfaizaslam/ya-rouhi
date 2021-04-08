#%%

d = {
    "mathew": "blue",
    "rachel": "green",
    "raymon": "red",
}
for k in d:
    print(k)

# %%
for k in d.keys():
    if k.startswith("r"):
        del d[k]
# %%
d = {k: d[k] for k in d if not k.startswith("r")}

# %%
print(d)
# %%
from collections import defaultdict

colors = ["red", "green", "red", "blue", "green", "red"]

d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)
# %%
from collections import defaultdict

names = ["raymond", "rachel", "mathew", "roger", "betty", "melisa", "judity", "charlie"]
d = {}
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
# %%
