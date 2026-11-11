from typing import list

def count(sequence:list[int], item:int)->int:
    result = 0
    for i in sequence:
        if i == item:
            result +=1
    return result
