shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!


def compute_bill(food):
    total = 0
    for x in food:
        # 檢查有冇貨（庫存大過 0）
        if stock[x] > 0:
            total += prices[x]   # 加上價錢
            stock[x] -= 1        # 買咗之後，庫存要減 1
    return total
