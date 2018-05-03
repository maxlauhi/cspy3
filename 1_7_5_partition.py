def count_partitions(k, g):
    if k == 0:
        return 1
    elif k < 0:
        return 0
    elif g == 0:
        return 1
    else:
        return count_partitions(k-g, g) + count_partitions(k, g-1)
