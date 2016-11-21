def binary_search(array, start, end, element):
    middle = len(array) // 2
    if array[middle] == element:
        return array[middle]
    if array[middle] < element:
        return binary_search(array[middle:], end // 2, end, element)
    return binary_search(array[:middle], start, end, element)


def find_turning_point(array, start, end):
    middle = len(array) // 2
    if array[middle] > array[middle + 1] and \
            not array[middle] < array[middle - 1]:
        return array[middle]
    if array[middle] < array[middle + 1]:
        return find_turning_point(array[middle:], end // 2, end)
    return find_turning_point(array[:middle], start, end)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10, 6))
