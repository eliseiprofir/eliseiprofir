def merge_sort(array: list[int]) -> list[int] | None:
    if len(array) <= 1:
        return

    middle_point: int = len(array) // 2
    left_part: list = array[:middle_point]
    right_part: list = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index: int = 0
    right_array_index: int = 0
    sorted_index: int = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

    return array


if __name__ == '__main__':
    numbers: list = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:', numbers)
    print('Sorted array:', merge_sort(numbers))
