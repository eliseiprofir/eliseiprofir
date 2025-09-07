def merge_sort(lst: list[any]) -> list[any]:

    if len(lst) <= 1:
        return lst

    if len(lst) == 2:
        if lst[1] < lst[0]:
            lst[1], lst[0] = lst[0], lst[1]
        return lst

    mid: int = len(lst) // 2
    left_half: list[any] = merge_sort(lst[:mid])
    right_half: list[any] = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left: list[any], right: list[any]) -> list[any] :
    merged: list[any] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += right[j:]
    merged += left[i:]

    return merged


if __name__ == "__main__":
    print(merge_sort([3, 5, 4, 1, 2, 6]))
