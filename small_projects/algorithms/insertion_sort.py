def insertion_sort(lst: list[any]) -> list[any]:
    for i in range(1, len(lst)):
        key: any = lst[i]
        j: int = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == "__main__":
    print(insertion_sort([3, 5, 4, 1, 2, 6]))
