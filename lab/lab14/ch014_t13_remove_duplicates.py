def remove_duplicates(seq: list[int]) -> list[int]:
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result
