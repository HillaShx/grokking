def solution(arr, k):
    sums = []
    subsum = 0
    for win_end in range(len(arr)):
        subsum += arr[win_end]
        if win_end >= k-1:
            sums.append(subsum/k)
            subsum -= arr[win_end-(k-1)]
    return sums


input_data = {
    1: {
        "arr": [1, 3, 2, 6, -1, 4, 1, 8, 2],
        "k": 5
    }
}