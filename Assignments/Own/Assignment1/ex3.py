
def strings_filter(list: list[str], max_len: int) -> list[str]:
    return [str for str in list if (len(str) <= max_len)]

print(strings_filter(["Python", "hello", "C++"], 4))
print(strings_filter(["Python", "hello", "C++"], 6))