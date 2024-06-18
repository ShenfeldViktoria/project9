def remove_duplicates(l: list[int]) -> list[int]:
    d = {}
    result = []
    for v in l:
        if v not in d:
            d[v] = 1
            result.append(v)
    return result


def remove_duplicates(l: list[int]) -> list[int]:
    s = list(set(l))
    s.sort()
    return s


if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 3, 3, 3, 5, 5, 6]))
    print(remove_duplicates([1, 1, 2, 3, 3, 3, 5, 5, 6]))
