from utils import debug


def solution(arr, k):
    max_sum = -1
    subsum = 0
    for win_end in range(len(arr)):
        subsum += arr[win_end]
        if win_end >= k-1:
            debug(subsum=subsum)
            max_sum = max(subsum, max_sum)
            subsum -= arr[win_end-(k-1)]
    return max_sum


input_data = {
    1: {
        "arr": [1, 3, 2, 6, -1, 4, 1, 8, 2],
        "k": 5
    }
}