def cele(tup1, tup2):
    out_tup = ()
    for elem in tup1:
        if elem in tup2:
            out_tup += (elem,)
    return out_tup

print(cele((1, 2, 3, 4), (3, 4, 5, 6)))  # (3, 4)