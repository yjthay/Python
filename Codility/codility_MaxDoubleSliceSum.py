"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    if len(A) <= 3:
        return 0
    lr = []
    rl = []

    s = 0
    for value in A[1:-1]:
        s += value
        if s < 0:
            s = 0
        lr.append(s)

    s = 0
    for value in A[-2:0:-1]:
        s += value
        if s < 0:
            s = 0
        rl.append(s)

    max_s = 0
    for l, r in zip(lr, rl[-3::-1]):
        max_s = max(max_s, l + r)
    print(max_s, l, r)
    # rl = rl[::-1]
    # for i in range(0, len(lr) - 2):
    #     max_s = max(max_s, lr[i] + rl[i + 2])
    # return max_s

    pass


if __name__ == '__main__':
    print(solution([3, 2, 6, -1, 4, 5, -1, 2]))  # 17
