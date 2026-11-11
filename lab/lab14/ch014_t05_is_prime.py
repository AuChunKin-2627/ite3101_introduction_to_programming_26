def is_prim(x:int)->bool:
    if x < 2:
        return False
    else:
        for n in range(2, n - 1):
            if x % n == 0:
                return False
        return True