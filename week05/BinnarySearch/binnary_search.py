def binary_search(array, start, end, element, full_array=[]):
    if len(array) > len(full_array):
        res = array
    else:
        res = full_array
    if len(full_array) == 0:
        res = array
    middle = end // 2
    if array[middle] == element:
        return res.index(array[middle])
    if array[middle] > element:
        return binary_search(array[:middle], start,
                             len(array[:middle]), element, res)
    return binary_search(array[middle:], start,
                         len(array[middle:]), element, res)


def find_turning_point(array, start, end):
    print(array)
    index = 0
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            index = i + 1
            break
    return str(array) + "Turning point is {el} on index {i}.".format(el=array[index],
                                                        i=index)


print(find_turning_point([1, 2, 3, 3, 4, 3], 0, 4))
