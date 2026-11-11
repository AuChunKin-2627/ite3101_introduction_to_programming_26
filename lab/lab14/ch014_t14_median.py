def median(seq:list[int])->float:
    sorted_seq = sorted(seq)
    if len(sorted_seq) % 2 == 0:
        