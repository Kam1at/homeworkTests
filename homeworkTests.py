def get_val(collection, key, default=""):
    if collection == {}:
        return default
    for i in collection:
        return collection[i] if i == key else default
