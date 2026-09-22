def count_num_one(tup):
    count = 0
    for elem in tup:
        if elem == 1:
            count += 1
    return count

print(count_num_one((1, 2, 3, 1, 4, 1)))  # 3