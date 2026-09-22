def rm_list_range(in_list, low, high):
    out_list = []
    for i in in_list:
        if min(i) >= low and max(i) <= high:
            out_list.append(i)
    return out_list

print(rm_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17))