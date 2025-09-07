def bubble_sort(lst: list[any]) -> list[any]:
    length: int = len(lst)
    for i in range(length):
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort_optimized(lst: list[any]) -> list[any]:
    length: int = len(lst)
    for i in range(length):
        swap: bool = False
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        if not swap:
            break
    return lst


if __name__ == "__main__":
    print(bubble_sort([3, 5, 4, 1, 2, 6]))
    print(bubble_sort_optimized([3, 5, 4, 1, 2, 6]))
