def purify(seq:list[int])->list[int]:
    result = []
    for item in seq:
        if item % 2 == 0:
            result.append(item)
        