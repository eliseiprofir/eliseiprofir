def quick_sort(lst: list[any]) -> list[any]:

    if len(lst) <= 1:
        return lst

    pivot: any = lst[0]

    less: list[any] = [x for x in lst[1:] if x <= pivot]
    more: list[any] = [x for x in lst[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(more)


if __name__ == "__main__":
    print(quick_sort([8, 4, 3, 7, 6]))
