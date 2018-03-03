def GetSmallest(arr):
    smallest = arr[0]
    smallest_idx = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i

    return smallest_idx

def sel_sort(arr):
    result = []
    for i in range(len(arr)):
        idx = GetSmallest(arr)
        result.append(arr[idx])
        arr.pop(idx)

    return result

    #return [arr.pop(GetSmallest(arr)) for _ in range(len(arr))]


def sel_sort2(arr):
    result = []
    result = map(arr.pop(min(arr)), arr)
    print('type:', type(result))
    print('result:', result)
    return result



if __name__ == '__main__':
   x = [5, 3, 6, 2, 10]
   print('x:', x)
   sorted_x = sel_sort2(x)
   print('sorted:', sorted_x)
