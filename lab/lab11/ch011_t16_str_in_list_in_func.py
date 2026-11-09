n = ["Michael", "Lieberman"]
# Add your function here


def join_strings(words: list[str]):
    result = ""
    for item in words:
        result = result + item
    return result

print(join_strings(n))
