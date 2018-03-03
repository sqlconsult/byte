def sum_arr(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_arr(arr[1::])

def cnt_arr(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + cnt_arr(arr[1::])


if __name__ == '__main__':
    arr = [10, 5, 7, 9, 15, 6, 11, 8, 12, 2, 3]
    ans = sum_arr(arr)
    print('sum:', ans)

    ans = cnt_arr(arr)
    print('count:', ans)
