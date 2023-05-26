"""A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited."""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    left_pointer, right_pointer = 0, 2
    min_avg = sum(A[left_pointer:right_pointer])
    min_idx = 0
    while right_pointer < len(A):
        print(left_pointer, right_pointer, A[left_pointer:right_pointer])
        avg = sum(A[left_pointer:right_pointer]) / (right_pointer - left_pointer)
        if avg < min_avg:
            min_idx = left_pointer
            min_avg = avg
        incremental_right = (A[right_pointer] - avg) / (right_pointer - left_pointer + 1)
        incremental_left = (A[left_pointer] - avg) / (right_pointer - left_pointer + 1)
        # print(incremental_right, incremental_left)

        # if incremental_right > 0:
        if incremental_left > 0:
            left_pointer += 1
            right_pointer = max(left_pointer + 2, right_pointer)
            # keep right_pointer static
        elif incremental_right > 0:
            left_pointer = right_pointer - 1
            right_pointer = left_pointer + 2
        else:
            right_pointer += 1
    return min_idx


# return r


if __name__ == '__main__':
    print(solution([4, 2, 2, 5, 1, 5, 8]))  # 1
    # print(solution([4, 4, 2, 3.5, 4, 5, 1, 5, 8]))  # 2
    # print(solution([4, 4, 2, 2, 3.5, 4, 5, 1, 5, 8]))  # 2
    # print(solution([4, 4, 2, 2, 2, 4, 5, 1, 5, 8]))  # 2
    # print(solution([10, 10, 10, 1, 9, 1, 10, 10, 10]))  # 2
