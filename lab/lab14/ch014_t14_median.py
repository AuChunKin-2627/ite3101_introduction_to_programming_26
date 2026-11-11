def median(seq: list[int]) -> float:
    sorted_seq = sorted(seq)
    if len(sorted_seq) % 2 == 0:
        index_1 = len(sorted_seq) // 2 - 1
        index_2 = len(sorted_seq) // 2
        m = (sorted_seq[index_1]+[index_2]) /2.0
        return m
    else:
        