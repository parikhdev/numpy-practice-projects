# Figure out a way to store 9 and 9.0 as separate values in the set
# (You can take the help of built-in datatypes)

Collection = set()

# Collection.add(str(9))
# Collection.add(str(9.0))

Collection.add((9, int))
Collection.add((9.0, float))
print(Collection)

