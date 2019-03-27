import math


def find_max_cross_subarray(A, low, mid, high, recursion_depth):
    left_sum = -111111111111
    current_sum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        current_sum += A[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    right_sum = -111111111111
    current_sum = 0
    max_right = mid + 1
    for i in range(mid+1, high+1):
        current_sum += A[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(A, low, high, recursion_depth):
    if high == low:
        return low, high, A[low]

    mid = math.floor((high + low) / 2)
    left_low, left_high, left_sum = find_max_subarray(A, low, mid, recursion_depth+1)
    right_low, right_high, right_sum = find_max_subarray(A, mid+1, high, recursion_depth+1)
    cross_low, cross_high, cross_sum = find_max_cross_subarray(A, low, mid, high, recursion_depth)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum

    if recursion_depth == 0:
        print(1)

    return cross_low, cross_high, cross_sum


def make_diff_arr(A):
    B = []
    for i in range(1, len(A)):
        el = A[i] - A[i - 1]
        B.append(el)
    return B


# A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
# A = make_diff_arr(A)
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

x, y, z = find_max_subarray(A, 0, len(A)-1, 0)
print(z)