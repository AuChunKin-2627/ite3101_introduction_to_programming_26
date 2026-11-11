def median(seq: list[int]) -> float:
    sorted_seq = sorted(seq)
    length = len(sorted_seq)
    if len(sorted_seq) % 2 == 0:
        index_1 = length // 2 - 1
        index_2 = length // 2
        return (sorted_seq[index_1]+[index_2]) / 2.0
    else:
        index = length // 2
        return sorted_seq[index]
