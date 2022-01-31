def keys_with_top_values(DICT):
    v = list(DICT.values())
    k = list(DICT.keys())
    
    print(k[v.index(max(v))])